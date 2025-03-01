import reflex as rx

config = rx.Config(
    app_name="lab",
    tailwind={"plugins": ["tailwindcss-radix"]},
    telemetry_enabled=False,
)
