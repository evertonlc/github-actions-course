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

#### 6. [05-2-filter-activity-types.yaml](.github/workflows/05-2-filter-activity-types.yaml)
**Purpose:** Demonstrates filtering for PR closed events

**Key Concepts:**
- Handling pull request closure events
- Branch-specific filtering
- Post-merge or PR close automation

**Features:**
- Only runs on pull requests targeting the `main` branch
- Filtered to the `closed` activity type exclusively
- Useful for cleanup tasks, notifications, or post-merge actions
- Runs regardless of whether the PR was merged or closed without merging

**Trigger:** Pull request closed on main branch

---

#### 7. [06-context.yaml](.github/workflows/06-context.yaml)
**Purpose:** Demonstrates accessing and using GitHub Actions context objects

**Key Concepts:**
- Working with context objects (`github`, `env`, `vars`, `inputs`)
- Accessing workflow metadata and event information
- Environment variable scope and precedence
- Context availability in different workflow sections

**Features:**
- Displays common `github` context properties:
  - Event name, ref, SHA, actor, workflow name, run number/ID
- Shows environment variable precedence (workflow → job → step level)
- Demonstrates variable overriding at different scopes
- Retrieves repository and organization variables using `vars` context
- Dynamic run name using `inputs.debug` parameter
- Alternative syntax for accessing environment variables

**Trigger:** Manual dispatch only (with optional debug input)

---

#### 8. [07-expressions.yaml](.github/workflows/07-expressions.yaml)
**Purpose:** Shows how to use expressions for conditional execution

**Key Concepts:**
- Boolean logic in expressions
- Conditional step execution using `if`
- Combining multiple conditions with logical operators
- Ternary-like operations using `&&` and `||`

**Features:**
- Dynamic run name with conditional text (`ON` or `OFF` based on debug input)
- Conditional debug steps that only run when `inputs.debug` is true
- Multi-condition expressions combining input values and context data
- Demonstrates checking branch references with expressions
- Clean separation of debug and production output

**Trigger:** Manual dispatch only (with optional debug input)

---

#### 9. [08-variables.yaml](.github/workflows/08-variables.yaml)
**Purpose:** Demonstrates environment variables at different scopes and levels

**Key Concepts:**
- Variable definition at workflow, job, and step levels
- Variable scope and precedence rules
- Repository and organization variables
- Environment-specific variables
- Default values for undefined variables

**Features:**
- Three-level variable hierarchy demonstration:
  - Workflow-level environment variables
  - Job-level environment variables (override workflow level)
  - Step-level environment variables (override job level)
- Shows how to override variables at different scopes
- Accesses repository variables with `vars` context
- Environment-specific variables using `environment: prod`
- Demonstrates default value pattern: `${{ vars.UNDEFINED_VAR || 'default value' }}`

**Trigger:** Manual dispatch only

---

#### 10. [09-functions.yaml](.github/workflows/09-functions.yaml)
**Purpose:** Demonstrates built-in GitHub Actions functions and status check functions

**Key Concepts:**
- Status check functions (`success()`, `failure()`, `cancelled()`)
- Data manipulation functions (`toJSON()`, `contains()`)
- Conditional execution based on step outcomes
- Working with complex event data structures

**Features:**
- Accesses pull request title and labels from event payload
- Uses `toJSON()` to pretty-print complex objects
- Demonstrates status check functions:
  - `success()`: Runs only if previous steps succeeded
  - `failure()`: Runs only if any previous step failed
  - `cancelled()`: Runs only if workflow was cancelled
  - `!cancelled()`: Runs always except when cancelled
- Shows `contains()` function for string matching in PR titles
- Combines multiple conditions with logical operators
- Practical example of conditional cleanup or notification steps

**Trigger:** Pull request events and manual dispatch

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
- **05-2-filter-activity-types.yaml**: Runs when PRs are closed on main
- **09-functions.yaml**: Runs on pull request events and manual dispatch

## 📚 Learning Path

These workflows are organized to progressively teach GitHub Actions concepts:

1. **Start with Building Blocks** (01) - Learn workflow, job, and step structure
2. **Understand Events** (02) - Learn what can trigger workflows
3. **Explore Runners** (03) - Learn about different execution environments
4. **Use Actions** (04) - Learn to leverage pre-built actions
5. **Master Filters** (05) - Learn to optimize when workflows run
6. **Work with Context** (06) - Learn to access workflow metadata and context objects
7. **Apply Expressions** (07) - Learn conditional logic and dynamic behavior
8. **Manage Variables** (08) - Learn variable scopes and environment configuration
9. **Use Functions** (09) - Learn built-in functions and status checks

## 🛠️ Project Structure

```
.github/
└── workflows/
    ├── 01-building-blocks.yaml
    ├── 02-workflow-event.yaml
    ├── 03-workflow-runners.yaml
    ├── 04-using-actions.yaml
    ├── 05-1-filter-activity-types.yaml
    ├── 05-2-filter-activity-types.yaml
    ├── 06-context.yaml
    ├── 07-expressions.yaml
    ├── 08-variables.yaml
    └── 09-functions.yaml

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