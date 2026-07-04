# Deployment Guide

This guide walks you through deploying your PassMark e-commerce platform to production.

## Frontend Deployment (Vercel)

Vercel is the easiest way to deploy Next.js apps.

### Step 1: Push to GitHub
Ensure your code is pushed to your GitHub repository:
```bash
git add .
git commit -m "Ready for production deployment"
git push origin main
```

### Step 2: Connect to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New..." → "Project"
3. Select your PassMark repository
4. Set the root directory to `./apps/frontend`
5. Add environment variables:
   - `NEXT_PUBLIC_API_URL`: Your backend API URL

### Step 3: Deploy
Click "Deploy" and your frontend will be live!

---

## Backend Deployment (Railway)

Railway makes backend deployment simple.

### Step 1: Connect Railway
1. Go to [railway.app](https://railway.app)
2. Create a new project
3. Select "Deploy from GitHub"
4. Choose your PassMark repository

### Step 2: Configure Railway
1. Set the root directory to `./apps/backend`
2. Set environment variables:
   - `PORT`: 5000
   - `NODE_ENV`: production
   - `DATABASE_URL`: Your MongoDB connection string
   - `JWT_SECRET`: Generate a secure secret

### Step 3: Deploy
Railway will automatically deploy when you push to main!

---

## Backend Deployment (Render.com)

Alternative to Railway.

### Step 1: Create New Service
1. Go to [render.com](https://render.com)
2. Click "New+" → "Web Service"
3. Connect your GitHub repository

### Step 2: Configure
- **Runtime**: Node
- **Root Directory**: `apps/backend`
- **Build Command**: `npm install && npm run build`
- **Start Command**: `npm start`

### Step 3: Set Environment Variables
Add all required environment variables in the Render dashboard.

---

## Database Setup (MongoDB Atlas)

### Step 1: Create MongoDB Atlas Account
1. Go to [mongodb.com/cloud/atlas](https://mongodb.com/cloud/atlas)
2. Sign up for a free account

### Step 2: Create a Cluster
1. Create a new project
2. Create a free tier cluster
3. Add a database user with username/password
4. Whitelist your IP or allow all IPs (0.0.0.0/0) for testing

### Step 3: Get Connection String
1. Click "Connect"
2. Choose "Connect your application"
3. Copy the connection string
4. Replace `<password>` with your database user password

### Step 4: Add to Backend
Add to your backend `.env`:
```
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/passmark?retryWrites=true&w=majority
```

---

## Domain Setup

### Adding Custom Domain (Frontend)
1. Go to Vercel project settings
2. Click "Domains"
3. Enter your custom domain
4. Follow DNS configuration instructions

### Adding Custom Domain (Backend)
Same process in Railway/Render settings.

---

## Production Checklist

- [ ] Frontend deployed and accessible
- [ ] Backend API deployed and accessible
- [ ] MongoDB database configured
- [ ] Environment variables set in production
- [ ] API endpoints tested
- [ ] SSL certificates installed
- [ ] Database backups configured
- [ ] Error logging set up
- [ ] Analytics enabled
- [ ] Email service configured (for orders)

---

## Monitoring & Maintenance

### View Logs
**Vercel**: Dashboard → Logs
**Railway**: Dashboard → Logs
**Render**: Dashboard → Logs

### Update Code
Push to main branch - deployment will automatically trigger!

### Rollback
Both platforms maintain deployment history for quick rollbacks.

---

## Performance Tips

1. **Enable Caching** in Vercel settings
2. **Use CDN** for static assets
3. **Optimize Images** with Next.js Image component
4. **Database Indexes** for frequently queried fields
5. **Compress Assets** with gzip

---

## Troubleshooting

### Backend not connecting to database?
- Check MongoDB Atlas connection string
- Verify IP whitelist in MongoDB Atlas
- Check credentials in .env

### Frontend can't reach API?
- Verify `NEXT_PUBLIC_API_URL` is set correctly
- Check CORS settings in backend
- Ensure backend is running

### Build failing?
- Check build logs in platform dashboard
- Verify Node version compatibility (18+)
- Ensure all dependencies are installed

---

## Cost Estimation

- **Vercel**: Free tier for Next.js (pay as you grow)
- **Railway**: $5/month + usage
- **Render**: Free tier available
- **MongoDB Atlas**: Free tier (512MB storage)

**Total for startup**: $5-10/month! 🎉

---

## Support

For deployment issues:
- Check platform documentation
- Review build/deployment logs
- Open a GitHub issue
