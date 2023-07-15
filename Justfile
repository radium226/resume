generate-keys:
    mkdir -p "keys"
    test -f "keys/private.key" || age-keygen -o "keys/private.key"
    sed -rne 's,^# public key: (.*)$,\1,p' "keys/private.key" >"keys/public.key"
    { gh secret list | grep -q "PRIVATE_KEY" ; } || gh secret set "PRIVATE_KEY" <"keys/private.key" 


encrypt-secrets:
    SOPS_AGE_RECIPIENTS="$( <"keys/public.key" )" \
        sops \
            --encrypted-regex "last_name" \
            --encrypt \
            --in-place \
                "sensitive.yml"


decrypt-secrets:
    SOPS_AGE_KEY_FILE="keys/private.key" \
        sops \
            --decrypt \
            --in-place \
                "sensitive.yml"
