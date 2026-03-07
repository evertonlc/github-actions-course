Repository containing all the examples and nodes for the [GitHub Actions: The Complete Guide from Beginner to Expert](https://www.udemy.com/course/mastering-github-actions-beginner-to-expert) course

## GitHub Actions Workflows Documentation

This repository contains several workflow examples demonstrating different GitHub Actions concepts and features. All workflows are located in the `.github/workflows/` directory.

### 📋 Workflow Files Overview

#### 1. [01-building-blocks.yaml](.github/workflows/01-building-blocks.yaml)
**Purpose:** Demonstrates the fundamental building blocks of GitHub Actions

**Key Concepts:**
- Basic workflow structure with jobs and steps
- Manual triggering using `workflow_dispatch`
- Multiple independent jobs (`echo-hello` and `echo-goodbye`)
- Error handling and failure behavior

**Features:**
- Two separate jobs running on `ubuntu-latest`
- Demonstrates how a failed step affects subsequent steps and workflow status
- Shows that when a step fails:
  - Remaining steps in the job will not run
  - The job will be marked as failed
  - Subsequent dependent jobs will not run

**Trigger:** Manual dispatch only

---

#### 2. [02-workflow-event.yaml](.github/workflows/02-workflow-event.yaml)
**Purpose:** Explores different workflow event triggers

**Key Concepts:**
- Multiple trigger types (pull requests, manual dispatch, scheduled runs)
- Using `github.event_name` context variable
- Syntax considerations for mixing trigger types

**Features:**
- Triggered by: `pull_request`, `workflow_dispatch`
- Commented example of `schedule` trigger with cron expression
- Displays which event triggered the workflow execution

**Trigger:** Pull request events and manual dispatch

---

#### 3. [03-workflow-runners.yaml](.github/workflows/03-workflow-runners.yaml)
**Purpose:** Demonstrates running workflows on different operating systems

**Key Concepts:**
- Multi-platform testing
- Runner selection using `runs-on`
- Accessing runner environment variables

**Features:**
- Three parallel jobs, each on a different OS:
  - `ubuntu-echo`: Runs on Ubuntu Linux
  - `windows-echo`: Runs on Windows (uses bash shell explicitly)
  - `macos-echo`: Runs on macOS
- Each job displays the runner's operating system using `$RUNNER_OS`

**Trigger:** Manual dispatch only

---

#### 4. [04-using-actions.yaml](.github/workflows/04-using-actions.yaml)
**Purpose:** Shows how to use pre-built actions from GitHub Marketplace

**Key Concepts:**
- Using actions with the `uses` keyword
- Configuring actions with parameters (`with`)
- Working directory configuration
- Building and testing a React application

**Features:**
- Uses `actions/checkout@v6` to clone the repository
- Uses `actions/setup-node@v6` to set up Node.js 20.x
- Sets default working directory to `04-using-actions/react-app`
- Installs dependencies with `npm ci`
- Runs unit tests with `npm run test`

**Trigger:** Manual dispatch only

---

#### 5. [05-1-filter-activity-types.yaml](.github/workflows/05-1-filter-activity-types.yaml)
**Purpose:** Demonstrates event filtering and activity type specifications

**Key Concepts:**
- Branch filtering for pull requests
- Activity type filtering
- Targeted workflow execution

**Features:**
- Only runs on pull requests targeting the `main` branch
- Filtered to specific activity types: `opened` and `synchronize`
- Prevents unnecessary workflow runs on other PR activities (e.g., labeled, closed)

**Trigger:** Pull request opened or synchronized (new commits pushed) to main branch

---

## 🚀 How to Use These Workflows

### Running Workflows Manually
Most workflows can be triggered manually using workflow_dispatch:
1. Go to the **Actions** tab in GitHub
2. Select the workflow you want to run
3. Click **Run workflow**
4. Choose the branch and click **Run workflow**

### Automatic Triggers
Some workflows run automatically:
- **02-workflow-event.yaml**: Runs on pull request events
- **05-1-filter-activity-types.yaml**: Runs when PRs are opened or updated against main

## 📚 Learning Path

These workflows are organized to progressively teach GitHub Actions concepts:

1. **Start with Building Blocks** (01) - Learn workflow, job, and step structure
2. **Understand Events** (02) - Learn what can trigger workflows
3. **Explore Runners** (03) - Learn about different execution environments
4. **Use Actions** (04) - Learn to leverage pre-built actions
5. **Master Filters** (05) - Learn to optimize when workflows run

## 🛠️ Project Structure

```
.github/
└── workflows/
    ├── 01-building-blocks.yaml
    ├── 02-workflow-event.yaml
    ├── 03-workflow-runners.yaml
    ├── 04-using-actions.yaml
    └── 05-1-filter-activity-types.yaml

04-using-actions/
└── react-app/
    ├── src/
    ├── public/
    └── package.json
```

## 📖 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)