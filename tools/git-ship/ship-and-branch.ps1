$ErrorActionPreference = "Stop"

$originalBranch = (git rev-parse --abbrev-ref HEAD).Trim()
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$branchName = "ship-$timestamp"

git checkout -b $branchName
git add .
git commit -m "Ship-$timestamp"
git push -u origin $branchName

if ((git status -sb) -match "ahead") {
  git push origin $branchName
}
