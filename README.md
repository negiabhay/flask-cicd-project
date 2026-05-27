# 💳 PayEasy CI/CD Pipeline

![CI/CD Pipeline](https://github.com/negiabhay/payeasy-cicd-project/actions/workflows/.yml/badge.svg)

A production-grade CI/CD pipeline built with **GitHub Actions** that automatically tests, builds, and deploys a Python application to **AWS EC2** on every code push, pull request, and on a weekly schedule.

---

## 📌 Project Overview

This project demonstrates a complete CI/CD workflow for a Python payment processing application — built **independently** as a hands-on DevOps practice project.

Every time code is pushed to the `main` branch or a pull request is opened, the pipeline automatically:
1. Runs tests across multiple Python versions simultaneously
2. Packages the application into a deployable artifact
3. Deploys it to an AWS EC2 server via SSH

---

## 🏗️ Pipeline Architecture

```
Push to main / Pull Request / Every Monday 9am
        │
        ▼
┌─────────────────────────────────┐
│         TEST JOB (Matrix)       │
│  ┌──────────┐  ┌──────────┐    │
│  │Python 3.9│  │Python3.10│    │
│  └──────────┘  └──────────┘    │
│       ┌──────────┐             │
│       │Python3.11│             │
│       └──────────┘             │
│   All 3 run simultaneously ⚡  │
└─────────────────────────────────┘
        │
        │ only if ALL tests pass
        ▼
┌─────────────────────────────────┐
│           BUILD JOB             │
│  • Packages app into .zip       │
│  • Prints app info from secrets │
│  • Uploads artifact to GitHub   │
│  • Retained for 5 days          │
└─────────────────────────────────┘
        │
        │ only if build passes
        ▼
┌─────────────────────────────────┐
│           DEPLOY JOB            │
│  • Downloads artifact           │
│  • Copies to EC2 via SCP        │
│  • SSHes into EC2               │
│  • Installs dependencies        │
│  • Deploys application          │
└─────────────────────────────────┘
        │
        ▼
   🌐 App Live on EC2!
```

---

## ⚙️ Pipeline Features

| Feature | Details |
|---|---|
| **CI Trigger** | Automatic on push to `main` branch |
| **PR Trigger** | Runs on every pull request targeting `main` |
| **Scheduled Trigger** | Runs every Monday at 9am automatically |
| **Matrix Testing** | Tests on Python 3.9, 3.10, 3.11 simultaneously |
| **Fail Fast** | Disabled — all matrix jobs complete for full visibility |
| **Job Dependencies** | `build` only runs if ALL tests pass, `deploy` only runs if build passes |
| **Artifacts** | Build output uploaded to GitHub with 5-day retention |
| **Secrets Management** | SSH keys and credentials stored in GitHub Secrets — never hardcoded |
| **Real Deployment** | Automatically deploys to AWS EC2 via SCP + SSH |

---

## 🛠️ Tech Stack

- **CI/CD:** GitHub Actions
- **Language:** Python 3.9 / 3.10 / 3.11
- **Testing:** pytest
- **Cloud:** AWS EC2 (Ubuntu 22.04)
- **Deployment:** appleboy/scp-action + appleboy/ssh-action

---

## 📁 Project Structure

```
payeasy-cicd-project/
├── app.py                          # Application logic
├── test_app.py                     # pytest test cases
├── requirements.txt                # Python dependencies
└── .github/
    └── workflows/
        └── .yml                    # GitHub Actions workflow
```

---

## 🔐 GitHub Secrets Required

| Secret Name | Description |
|---|---|
| `APP_VERSION` | Current version of the application |
| `EC2_HOST` | Public IP address of your EC2 instance |
| `EC2_USERNAME` | SSH username (e.g. `ubuntu`) |
| `EC2_SSH_KEY` | Contents of your EC2 `.pem` private key file |

> ⚠️ Never hardcode sensitive values in your pipeline file. Always use GitHub Secrets.

---

## 📋 Pipeline Walkthrough

### 1. Test Job
- Triggered on push to `main`, pull requests, and every Monday at 9am
- Runs on a fresh Ubuntu runner for each Python version
- Downloads code, installs Python, installs dependencies
- Runs `pytest` — if any test fails, pipeline stops here
- `fail-fast: false` ensures all versions complete even if one fails

### 2. Build Job
- Only starts after ALL matrix test jobs pass
- Uses `APP_NAME` environment variable for app identification
- Uses `APP_VERSION` secret for version tracking
- Packages `app.py` and `requirements.txt` into `payeasy.zip`
- Uploads the zip as a GitHub Actions artifact (retained for 5 days)

### 3. Deploy Job
- Only starts after the build job passes
- Downloads the artifact onto a fresh runner
- Copies `payeasy.zip` to EC2 server using SCP
- SSHes into EC2 and:
  - Installs `unzip` and `pip` if not present
  - Unzips the application
  - Installs Python dependencies
  - Confirms successful deployment

---

## 💡 Key Concepts Demonstrated

- **Continuous Integration** — automated testing on every push and PR
- **Continuous Deployment** — automatic deployment to real AWS EC2 server
- **Multiple Triggers** — push, pull request and scheduled cron trigger
- **Matrix Builds** — parallel testing across multiple Python versions
- **Job Dependencies** — controlled pipeline flow using `needs:`
- **Artifact Management** — passing build outputs between isolated jobs
- **Secrets Management** — secure handling of SSH keys and credentials
- **Infrastructure Automation** — server setup handled entirely by pipeline

---

## 👤 Author

**Abhay Negi**
- GitHub: [@negiabhay](https://github.com/negiabhay)
- LinkedIn: [a-negi](https://linkedin.com/in/a-negi)

---

> 💬 *"This pipeline was built independently as part of my DevOps learning journey — writing the complete workflow file from scratch, debugging my own mistakes, and successfully deploying to a real AWS EC2 server without any assistance."*
