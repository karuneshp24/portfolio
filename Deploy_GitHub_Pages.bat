@echo off
title Publish Portfolio to GitHub Pages (24/7 Permanent Free Hosting)
color 0B
echo =========================================================================
echo          KARUNESH P - GITHUB PAGES PERMANENT DEPLOYMENT HELPER
echo =========================================================================
echo.
echo This script will publish your portfolio to GitHub Pages so it remains:
echo   - 24/7 All-Time Active (never turns off even if your computer is shut)
echo   - Formal URL: https://karuneshp24.github.io/portfolio
echo   - No random numbers, official software engineer domain
echo.
echo Step 1: Create a new empty repository named 'portfolio' on GitHub:
echo         https://github.com/new
echo         (Leave "Initialize this repository with README" UNCHECKED)
echo.
echo Step 2: Press any key below once the repository is created on github.com
pause
echo.
echo Configuring remote and pushing to GitHub...
git branch -M main
git remote remove origin >nul 2>&1
git remote add origin https://github.com/karuneshp24/portfolio.git
git push -u origin main

echo.
echo =========================================================================
echo Step 3: Enable GitHub Pages in your repository settings:
echo         1. Open: https://github.com/karuneshp24/portfolio/settings/pages
echo         2. Under "Build and deployment" -> Source: select "Deploy from a branch"
echo         3. Select Branch: "main" and folder "/ (root)" -> Click "Save"
echo.
echo Your formal website will be live 24/7 at:
echo https://karuneshp24.github.io/portfolio/
echo =========================================================================
echo.
pause
