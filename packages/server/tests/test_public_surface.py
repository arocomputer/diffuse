from __future__ import annotations

import hashlib
import hmac

import httpx
import pytest
from diffuse.api.app import app
from diffuse.repository.policy.models import RepositoryConfig


@pytest.mark.anyio
async def test_unimplemented_public_surfaces_are_not_mounted():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://testserver"
    ) as client:
        for path in (
            "/mcp",
            "/api/v1/repositories",
            "/auth/cli",
            "/auth/github/callback",
            "/setup",
            "/docs",
            "/openapi.json",
        ):
            assert (await client.get(path)).status_code == 404


@pytest.mark.anyio
async def test_signed_github_webhook_ingress_is_mounted(monkeypatch: pytest.MonkeyPatch):
    secret = "webhook-contract-test-secret"
    body = b"{}"
    signature = "sha256=" + hmac.new(
        secret.encode(), body, hashlib.sha256
    ).hexdigest()
    monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", secret)

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://testserver"
    ) as client:
        response = await client.post(
            "/webhook/github",
            content=body,
            headers={
                "x-github-event": "ping",
                "x-github-delivery": "webhook-contract-test",
                "x-hub-signature-256": signature,
            },
        )

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unimplemented_automatic_approval_configuration_is_rejected():
    with pytest.raises(ValueError, match="auto_approval is not implemented"):
        RepositoryConfig.model_validate(
            {"version": 1, "auto_approval": {"enabled": True}}
        )


def test_unimplemented_agent_change_configuration_is_rejected():
    with pytest.raises(ValueError, match="fix_with_agent is not implemented"):
        RepositoryConfig.model_validate(
            {"version": 1, "review": {"fix_with_agent": True}}
        )
