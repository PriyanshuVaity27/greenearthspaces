import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

print("🔍 Testing environment variables...")

# List of keys you expect
required_vars = [
    "DATABASE_URL",
    "SECRET_KEY",
    "ALGORITHM",
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_KEY",
    "SUPABASE_BUCKET"
]

# Check each
for var in required_vars:
    value = os.getenv(var)
    if value:
        print(f"✅ {var} loaded: {value[:10]}...")  # print first 10 chars only
    else:
        print(f"❌ {var} is MISSING!")
