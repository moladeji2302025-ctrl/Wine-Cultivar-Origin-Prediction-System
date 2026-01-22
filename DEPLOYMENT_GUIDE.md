# Vercel Deployment Guide for Wine Cultivar Prediction System

## Prerequisites
- GitHub account with this repository
- Vercel account (sign up at vercel.com)

## Deployment Steps

### 1. Connect Repository to Vercel
1. Go to https://vercel.com
2. Click "Add New Project"
3. Import your GitHub repository: `moladeji2302025-ctrl/Wine-Cultivar-Origin-Prediction-System`

### 2. Configure Project Settings
- **Framework Preset**: Select "Other"
- **Root Directory**: Leave as default (root)
- **Build Command**: Leave empty or use `pip install -r requirements.txt`
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### 3. Environment Variables (Optional)
Add the following environment variable if needed:
- Key: `FLASK_DEBUG`
- Value: `false`

### 4. Deploy
Click "Deploy" and wait for the deployment to complete.

## Troubleshooting

### Error: "Failed to run 'uv add'"
This error occurs when Vercel tries to use `uv` package manager instead of `pip`.

**Solution**:
1. Make sure your `requirements.txt` has specific version numbers (which it does)
2. Add a `vercel.json` file (already created) to configure the build process
3. Ensure all dependencies are compatible

### Alternative: Manual Deployment
If Vercel deployment fails, you can deploy using other platforms:
- **Render**: Free tier available, great for Flask apps
- **Railway**: Easy deployment with GitHub integration
- **PythonAnywhere**: Specifically designed for Python web apps
- **Heroku**: Supports Python/Flask applications

## Post-Deployment
After successful deployment:
1. Copy the deployment URL (e.g., https://your-app.vercel.app)
2. Update `WineCultivar_hosted_webGUI_link.txt` with:
   - Your name
   - Your matric number
   - The deployment URL
3. Test the application by accessing the URL

## Testing the Deployed App
1. Navigate to the deployment URL
2. Enter sample wine chemical properties
3. Click "Predict Cultivar"
4. Verify the prediction is displayed correctly

## Sample Input Values for Testing
You can use these sample values to test the deployed application:

- **Flavanoids**: 2.5
- **Color Intensity**: 5.0
- **Alcohol**: 13.0
- **Proline**: 900
- **OD280/OD315 of Diluted Wines**: 2.5
- **Hue**: 1.0

Expected result: Should predict one of the three cultivar classes with high confidence.
