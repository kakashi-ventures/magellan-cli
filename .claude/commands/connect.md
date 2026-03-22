---
description: "Connect your MAGELLAN web profile to this CLI. Usage: /connect <contributor-key>"
allowed-tools: Bash, WebFetch
---

# Connect to MAGELLAN Web Profile

## User Input
$ARGUMENTS

## Step 1: Validate Key

The contributor key must start with `mgln_`. If no key is provided or the format is wrong, show:

> To get your contributor key:
> 1. Create an account at https://magellan-discover.ai/sign-in
> 2. Go to your profile at https://magellan-discover.ai/profile
> 3. Generate a contributor key
> 4. Run: `/connect mgln_your_key_here`

## Step 2: Verify Key

Call the web API to verify the key:

```bash
curl -s "https://magellan-discover.ai/api/contributor/verify?key=$KEY" 2>/dev/null
```

If the response contains `"valid":true`, extract the `name` field.
If the response contains `"valid":false` or the request fails, show an error.

## Step 3: Save Config

```bash
mkdir -p .magellan
cat > .magellan/config.json << EOF
{
  "contributor_key": "$KEY",
  "display_name": "$NAME",
  "web_url": "https://magellan-discover.ai"
}
EOF
```

## Step 4: Confirm

> Connected as **$NAME**. Your discoveries will be attributed to your MAGELLAN profile.
> Profile: https://magellan-discover.ai/profile
