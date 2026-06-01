# MyApp — CI/CD Pipeline Demo

## What this project demonstrates
End-to-end CI/CD pipeline: code push → automated test → Docker build → deployment.
Zero manual steps after `git push`.

## Architecture
## Stack
- **Gitea** — self-hosted Git server (local GitHub replacement)
- **Jenkins** — CI/CD engine with pipeline-as-code (Jenkinsfile)
- **Docker** — containerised build, test, and runtime environment
- **Python/Flask** — demo application with pytest test suite

## Pipeline stages
| Stage | What happens |
|---|---|
| Test | Runs pytest inside isolated Docker container |
| Build | Builds versioned Docker image `myapp:BUILD_NUMBER` |
| Deploy | Replaces running container with new version |

## Key decisions made
- Tests run inside Docker — pipeline has zero host dependencies
- Dedicated `Dockerfile.test` separates test and production images
- `notifyCommit` webhook bypasses Jenkins CSRF — cleaner than API tokens
- Static IP on VM ensures webhook URL never changes

## Lessons learned
- Jenkins CSRF protection blocks naive webhook calls — solved with Git notifyCommit token
- Docker-in-Docker via socket mount requires Docker CLI installed in Jenkins container
- Branch naming mismatch (master vs main) is a common real-world gotcha

## How to run locally
```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
curl http://localhost:5000/health
```
# demo Mon Jun  1 07:02:43 AM UTC 2026
# demo Mon Jun  1 07:03:55 AM UTC 2026
# demo Mon Jun  1 07:10:49 AM UTC 2026
# demo Mon Jun  1 07:16:59 AM UTC 2026
# restart Mon Jun  1 07:20:07 AM UTC 2026
# demo Mon Jun  1 07:27:35 AM UTC 2026
# demo Mon Jun  1 07:31:07 AM UTC 2026
# demo Mon Jun  1 07:32:54 AM UTC 2026
# demo Mon Jun  1 07:41:24 AM UTC 2026
# demo Mon Jun  1 08:10:34 AM UTC 2026
