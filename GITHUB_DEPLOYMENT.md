# GitHub Deployment Guide

Your Loan Approval Predictor project is now ready to upload to GitHub. Follow these steps to push your code to GitHub.

## Prerequisites

- GitHub account (create at https://github.com)
- Git installed on your system ✓ (already installed)
- Git configured with your credentials ✓ (already configured)

## Step-by-Step Instructions

### Option 1: Using HTTPS (Recommended for beginners)

#### 1. Create a New Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the **+** icon in the top-right corner
3. Select **New repository**
4. Fill in the following:
   - **Repository name**: `loan-approval-predictor` (or any name you prefer)
   - **Description**: "Loan Approval Predictor - Flask web app with ML model"
   - **Visibility**: Public (if you want others to see it) or Private
   - **Do NOT** initialize with README, .gitignore, or license (we already have them)
5. Click **Create repository**

#### 2. Add Remote and Push

After creating the repository, GitHub will show you commands to run. Copy these commands or use the ones below, replacing `YOUR_USERNAME` with your GitHub username:

```bash
cd C:\Users\ACER\Desktop\loan_web_app

# Add the remote repository
git remote add origin https://github.com/YOUR_USERNAME/loan-approval-predictor.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

When prompted for a password, use your **Personal Access Token** (see below).

---

### Option 2: Using SSH (More Secure)

If you prefer SSH authentication, follow these steps:

#### 1. Generate SSH Key (if you don't have one)

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter to accept default location, and optionally set a passphrase.

#### 2. Add SSH Key to GitHub

1. Copy the public key:
```bash
cat ~/.ssh/id_ed25519.pub
```

2. Go to GitHub Settings → [SSH and GPG keys](https://github.com/settings/keys)
3. Click **New SSH key**
4. Paste your public key and click **Add SSH key**

#### 3. Create Repository and Push

```bash
cd C:\Users\ACER\Desktop\loan_web_app

# Add the remote repository (using SSH)
git remote add origin git@github.com:YOUR_USERNAME/loan-approval-predictor.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## Creating a Personal Access Token (for HTTPS)

If using HTTPS and GitHub requires authentication:

1. Go to GitHub Settings → [Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click **Generate new token** → **Generate new token (classic)**
3. Give it a name (e.g., "Git CLI Access")
4. Select scopes:
   - ✓ `repo` (full control of private repositories)
   - ✓ `workflow` (if needed)
5. Click **Generate token**
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when pushing

---

## After Pushing to GitHub

1. Verify your repository is online:
   - Visit `https://github.com/YOUR_USERNAME/loan-approval-predictor`

2. Update repository settings if desired:
   - Add a proper README.md
   - Add topics/tags for discoverability
   - Configure branch protection rules
   - Add a license

---

## Useful Git Commands

### Check Repository Status
```bash
cd C:\Users\ACER\Desktop\loan_web_app
git status
```

### View Commit History
```bash
git log --oneline
```

### Make Changes and Push

After modifications:
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

### Pull Updates from GitHub
```bash
git pull origin main
```

---

## Project Files Included

Your repository includes:

- **flask_app.py** - Flask backend server
- **app.py** & **app1.py** - Alternative app files (for reference)
- **requirements.txt** - Python dependencies
- **templates/index.html** - HTML template
- **static/style.css** - CSS styling
- **static/script.js** - JavaScript interactivity
- **README_WEB.md** - Application documentation
- **decision_tree_model.pkl** - Trained ML model (excluded from git if large)
- **.gitignore** - Files to exclude from version control

---

## Troubleshooting

### Error: "fatal: 'origin' does not appear to be a 'git' repository"

You may have already added the remote. Check with:
```bash
git remote -v
```

If origin already exists, you can update it:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/loan-approval-predictor.git
```

### Error: "fatal: not a git repository"

Make sure you're in the correct directory:
```bash
cd C:\Users\ACER\Desktop\loan_web_app
```

### Error: "Permission denied (publickey)"

If using SSH and getting permission denied:
1. Make sure your SSH key is added to the SSH agent
2. Try using HTTPS instead
3. Verify the SSH key is added to your GitHub account

### Large File Warning

If `decision_tree_model.pkl` is very large (>100MB), GitHub may warn you. Consider using Git LFS:

```bash
# Install Git LFS
choco install git-lfs  # or brew install git-lfs on Mac

# Initialize Git LFS
git lfs install

# Track .pkl files
git lfs track "*.pkl"

# Add and commit
git add .gitattributes *.pkl
git commit -m "Add large model file with Git LFS"
```

---

## Next Steps

1. **Verify your code is online**: Check GitHub at your repository URL
2. **Share the link**: You can now share your GitHub repository with others
3. **Continue development**: Make changes locally, commit, and push
4. **Collaborate**: Invite others to contribute or fork your project
5. **Deploy**: Consider deploying on platforms like Heroku, Railway, or AWS
6. **CI/CD**: Add GitHub Actions for automated testing and deployment

---

## Additional Resources

- [GitHub Documentation](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [SSH Keys Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

**Project Created**: April 17, 2026
**Repository Structure**: Flask + HTML/CSS/JS
**Status**: Ready for GitHub upload
