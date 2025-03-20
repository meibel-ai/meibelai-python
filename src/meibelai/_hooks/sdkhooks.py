"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import httpx
from .types import (
    SDKInitHook,
    BeforeRequestContext,
    BeforeRequestHook,
    AfterSuccessContext,
    AfterSuccessHook,
    AfterErrorContext,
    AfterErrorHook,
    Hooks,
)
from .registration import init_hooks
from typing import List, Optional, Tuple
from meibelai.httpclient import HttpClient


class SDKHooks(Hooks):
    def __init__(self) -> None:
        self.sdk_init_hooks: List[SDKInitHook] = []
        self.before_request_hooks: List[BeforeRequestHook] = []
        self.after_success_hooks: List[AfterSuccessHook] = []
        self.after_error_hooks: List[AfterErrorHook] = []
        init_hooks(self)

    def register_sdk_init_hook(self, hook: SDKInitHook) -> None:
        self.sdk_init_hooks.append(hook)

    def register_before_request_hook(self, hook: BeforeRequestHook) -> None:
        self.before_request_hooks.append(hook)

    def register_after_success_hook(self, hook: AfterSuccessHook) -> None:
        self.after_success_hooks.append(hook)

    def register_after_error_hook(self, hook: AfterErrorHook) -> None:
        self.after_error_hooks.append(hook)

    def sdk_init(self, base_url: str, client: HttpClient) -> Tuple[str, HttpClient]:
        for hook in self.sdk_init_hooks:
            base_url, client = hook.sdk_init(base_url, client)
        return base_url, client

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        for hook in self.before_request_hooks:
            out = hook.before_request(hook_ctx, request)
            if isinstance(out, Exception):
                raise out
            request = out

        return request

    def after_success(
        self, hook_ctx: AfterSuccessContext, response: httpx.Response
    ) -> httpx.Response:
        for hook in self.after_success_hooks:
            out = hook.after_success(hook_ctx, response)
            if isinstance(out, Exception):
                raise out
            response = out
        return response

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception],
    ) -> Tuple[Optional[httpx.Response], Optional[Exception]]:
        for hook in self.after_error_hooks:
            result = hook.after_error(hook_ctx, response, error)
            if isinstance(result, Exception):
                raise result
            response, error = result
        return response, error
