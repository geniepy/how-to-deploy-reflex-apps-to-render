import reflex as rx
import os
# Get the port from the environment variable or fall back to 3000
port = int(os.environ.get("PORT", 3000))


config = rx.Config(
    app_name="deploy_reflex_render",
    frontend_port=port,
)