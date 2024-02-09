
CORS_SETTINGS = {
    "allow_origins": [
        "http://127.0.0.1:5173",  # Local development origin
        "https://algorithm-analyzer-frontend.onrender.com"  # Render deployed frontend origin
    ],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
