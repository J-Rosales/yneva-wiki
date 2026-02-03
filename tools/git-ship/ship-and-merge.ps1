$ErrorActionPreference = "Stop"

$originalBranch = (git rev-parse --abbrev-ref HEAD).Trim()
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$branchName = "ship-$timestamp"

git checkout -b $branchName
git add .
git commit -m "Ship-$timestamp"
git push -u origin $branchName

git fetch origin
git rebase origin/$originalBranch

git checkout $originalBranch
git merge --squash $branchName
git commit -m "Ship-$timestamp"

if ((git status -sb) -match "ahead") {
  git push origin $originalBranch
}
