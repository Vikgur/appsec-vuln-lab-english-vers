#!/usr/bin/env bash

set -euo pipefail

create_dir() {
    for dir in $@; do
        mkdir -p "$dir"
        if [ -z "$(ls -A "$dir")" ]; then
            touch "$dir/.gitkeep"
        fi
    done
}

# languages

# python

create_dir languages/python/web/flask/{sql-injection-unparameterized-query,command-injection-shell-execution,nosql-injection-operator-injection,ssti-user-input-template-render,path-traversal-directory-escape,insecure-file-upload-unrestricted-upload,unsafe-deserialization-pickle-rce,unsafe-yaml-load-object-deserialization,reflected-xss-unescaped-html-response,stored-xss-persistent-html-injection,csrf-state-changing-post-without-token,broken-authentication-session-fixation-and-weak-session-id,jwt-validation-missing-alg-and-claim-verification,idor-horizontal-privilege-escalation-object-access,vertical-privilege-escalation-missing-backend-role-enforcement,ssrf-internal-network-and-metadata-access,open-redirect-user-controlled-redirect-target,insecure-cryptography-weak-password-hash-and-random,hardcoded-secret-and-debug-information-leakage,dependency-risk-unpinned-versions-and-vulnerable-library-usage,race-condition-check-then-use-double-spend,race-condition-check-then-update-double-spend,resource-exhaustion-unbounded-upload-and-regex-redos}
touch $(echo languages/python/web/flask/{sql-injection-unparameterized-query,command-injection-shell-execution,nosql-injection-operator-injection,ssti-user-input-template-render,path-traversal-directory-escape,insecure-file-upload-unrestricted-upload,unsafe-deserialization-pickle-rce,unsafe-yaml-load-object-deserialization,reflected-xss-unescaped-html-response,stored-xss-persistent-html-injection,csrf-state-changing-post-without-token,broken-authentication-session-fixation-and-weak-session-id,jwt-validation-missing-alg-and-claim-verification,idor-horizontal-privilege-escalation-object-access,vertical-privilege-escalation-missing-backend-role-enforcement,ssrf-internal-network-and-metadata-access,open-redirect-user-controlled-redirect-target,insecure-cryptography-weak-password-hash-and-random,hardcoded-secret-and-debug-information-leakage,dependency-risk-unpinned-versions-and-vulnerable-library-usage,race-condition-check-then-use-double-spend,race-condition-check-then-update-double-spend,resource-exhaustion-unbounded-upload-and-regex-redos}/{vuln_app.py,fixed_app.py,exploit_payload.txt,README.md})

create_dir languages/python/web/fastapi
create_dir languages/python/web/django
create_dir languages/python/cli/click-cli
create_dir languages/python/system

# javascript

create_dir languages/javascript/web/react
create_dir languages/javascript/cli/nodejs-script

# typescript

create_dir languages/typescript/web/react

# java

create_dir languages/java/web/spring-boot
create_dir languages/java/mobile/android

# dotnet

create_dir languages/dotnet/web/aspnetcore
create_dir languages/dotnet/mobile/uwp

# c

create_dir languages/c/system/buffer-overflow-stack
create_dir languages/c/system/format-string-vuln
create_dir languages/c/system/race-conditions
create_dir languages/c/embedded/freertos-irq-stack-overflow
create_dir languages/c/mobile/ios-c-extension/memory-corruption-in-c

# cpp

create_dir languages/cpp/system/use-after-free
create_dir languages/cpp/system/double-free
create_dir languages/cpp/system/vtable-hijacking
create_dir languages/cpp/embedded/arduino-cpp-memory-corruption
create_dir languages/cpp/mobile/android-ndk/jni-buffer-overflow

# erlang

create_dir languages/erlang/system/otp-process-race
create_dir languages/erlang/system/insecure-cookie-handling
create_dir languages/erlang/web/cowboy-http-smuggling

# go

create_dir languages/go/web/gin
create_dir languages/go/cli/cobra

# rust

create_dir languages/rust/system
create_dir languages/rust/cli/clap

# infrastructure

create_dir infrastructure/cloud/aws
create_dir infrastructure/cloud/gcp
create_dir infrastructure/cloud/azure
create_dir infrastructure/orchestration/kubernetes
create_dir infrastructure/orchestration/nomad
create_dir infrastructure/containerization/docker
create_dir infrastructure/containerization/podman
create_dir infrastructure/iac-and-config/terraform
create_dir infrastructure/iac-and-config/ansible
create_dir infrastructure/iac-and-config/puppet
create_dir infrastructure/iac-and-config/saltstack
create_dir infrastructure/iac-and-config/cloudformation

# devsecops

create_dir devsecops/sast/semgrep/python
touch devsecops/sast/semgrep/python/{sql-injection-unparameterized-query.yaml,command-injection-shell-execution.yaml,nosql-injection-operator-injection.yaml,ssti-user-input-template-render.yaml,path-traversal-directory-escape.yaml,insecure-file-upload-unrestricted-upload.yaml,unsafe-deserialization-pickle-rce.yaml,unsafe-yaml-load-object-deserialization.yaml,reflected-xss-unescaped-html-response.yaml,stored-xss-persistent-html-injection.yaml,csrf-state-changing-post-without-token.yaml,broken-authentication-session-fixation-and-weak-session-id.yaml,jwt-validation-missing-alg-and-claim-verification.yaml,idor-horizontal-privilege-escalation-object-access.yaml,vertical-privilege-escalation-missing-backend-role-enforcement.yaml,ssrf-internal-network-and-metadata-access.yaml,open-redirect-user-controlled-redirect-target.yaml,insecure-cryptography-weak-password-hash-and-random.yaml,hardcoded-secret-and-debug-information-leakage.yaml,dependency-risk-unpinned-versions-and-vulnerable-library-usage.yaml,race-condition-check-then-use-double-spend.yaml,race-condition-check-then-update-double-spend.yaml,resource-exhaustion-unbounded-upload-and-regex-redos.yaml}
create_dir devsecops/sast/semgrep/java
create_dir devsecops/sast/semgrep/dotnet
create_dir devsecops/sast/semgrep/go
create_dir devsecops/sast/sonarqube
create_dir devsecops/dast
create_dir devsecops/fuzzing
create_dir devsecops/secrets
create_dir devsecops/scripts
create_dir devsecops/sca
create_dir devsecops/iac-scanning
create_dir devsecops/ci-cd-pipelines

touch README.md
touch .gitignore

echo "Structure created in current repository."
