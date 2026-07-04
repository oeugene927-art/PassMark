# Quick Start Guide - PassMark E-Commerce Platform

## 🎉 Your e-commerce platform is ready!

Your PassMark repository now has a complete, production-ready e-commerce structure. Follow these steps to get it running locally.

## 📋 Prerequisites

- Node.js 18+ installed
- npm or yarn
- Git
- MongoDB Atlas account (free tier available)
- Stripe account (for payments)

## 🚀 Setup Instructions

### Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/oeugene927-art/PassMark.git
cd PassMark

# Install root dependencies
npm install

# Install workspace dependencies
cd apps/backend && npm install
cd ../frontend && npm install
cd ../..
```

### Step 2: Configure Environment Variables

**Backend Setup:**

1. Create `apps/backend/.env` from `.env.example`:

```bash
cp apps/backend/.env.example apps/backend/.env
```

2. Edit `apps/backend/.env` with your credentials:

```env
PORT=5000
NODE_ENV=development
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/passmark
JWT_SECRET=your_super_secret_jwt_key_here_minimum_32_characters_long
JWT_EXPIRE=7d
STRIPE_SECRET_KEY=sk_test_your_stripe_key
STRIPE_PUBLIC_KEY=pk_test_your_stripe_key
FRONTEND_URL=http://localhost:3000
```

**Frontend Setup:**

1. Create `apps/frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:5000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_your_stripe_key
```

### Step 3: Get Your Database & Payment Keys

**MongoDB Atlas:**
1. Go to [mongodb.com/cloud/atlas](https://mongodb.com/cloud/atlas)
2. Create a free cluster
3. Get your connection string
4. Add to `DATABASE_URL` in `.env`

**Stripe:**
1. Go to [stripe.com](https://stripe.com)
2. Create a test account
3. Get API keys from Dashboard
4. Add to `.env` files

### Step 4: Run the Application

**Option A: Run both servers together**

```bash
npm run dev
```

This starts:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

**Option B: Run separately**

```bash
# Terminal 1 - Backend
cd apps/backend
npm run dev

# Terminal 2 - Frontend
cd apps/frontend
npm run dev
```

### Step 5: Test the Application

1. Open http://localhost:3000
2. Click "Register" to create an account
3. Browse products
4. Add items to cart
5. Checkout (test Stripe integration)

## 📁 Project Structure

```
PassMark/
├── apps/
│   ├── backend/
│   │   ├── src/
│   │   │   ├── routes/       # API endpoints
│   │   │   ├── models/       # MongoDB schemas
│   │   │   ├── middleware/   # Auth, logging, etc
│   │   │   └── server.ts     # Main server file
│   │   ├── package.json
│   │   └── .env.example      # Environment variables template
│   │
│   └── frontend/
│       ├── src/
│       │   ├── app/          # Next.js pages
│       │   ├── components/   # React components
│       │   ├── store/        # Redux state management
│       │   ├── lib/          # Utilities & API client
│       │   └── styles/       # CSS files
│       ├── package.json
│       └── next.config.js
│
├── DEPLOYMENT.md             # Deployment instructions
├── CONTRIBUTING.md           # Contributing guidelines
└── package.json             # Root package.json
```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Products
- `GET /api/products` - Get all products
- `GET /api/products/:id` - Get product details
- `POST /api/products` - Create product (admin)
- `PUT /api/products/:id` - Update product (admin)
- `DELETE /api/products/:id` - Delete product (admin)

### Cart
- `GET /api/cart` - Get cart items
- `POST /api/cart/add` - Add to cart
- `DELETE /api/cart/:productId` - Remove from cart

### Orders
- `POST /api/orders` - Create order
- `GET /api/orders` - Get user orders
- `GET /api/orders/:id` - Get order details

### Users
- `GET /api/users/profile` - Get user profile
- `PUT /api/users/profile` - Update profile

## 🧪 Testing

### Test User Registration
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "firstName": "John",
    "lastName": "Doe"
  }'
```

### Test Get Products
```bash
curl http://localhost:5000/api/products
```

## 🚀 Deployment

For production deployment, see [DEPLOYMENT.md](./DEPLOYMENT.md)

**Quick deployment steps:**
1. Push code to GitHub
2. Deploy frontend to Vercel
3. Deploy backend to Railway or Render
4. Connect MongoDB Atlas
5. Set environment variables on each platform

## 📚 Technology Stack

**Frontend:**
- Next.js 14 - React framework
- TypeScript - Type safety
- Tailwind CSS - Styling
- Redux Toolkit - State management
- Axios - HTTP client

**Backend:**
- Node.js/Express - Server framework
- MongoDB - Database
- Mongoose - ODM
- JWT - Authentication
- Stripe - Payments

## 🔒 Security Features

✅ JWT authentication
✅ Password hashing with bcrypt
✅ CORS protection
✅ Rate limiting
✅ Environment variable management
✅ Secure API routes

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 5000 is in use
lsof -i :5000

# Kill process if needed
kill -9 <PID>
```

### Can't connect to MongoDB
```bash
# Verify connection string in .env
# Check MongoDB Atlas IP whitelist
# Test connection: mongosh "your_connection_string"
```

### Frontend can't reach API
```bash
# Verify NEXT_PUBLIC_API_URL is correct
# Check backend is running on port 5000
# Check browser console for CORS errors
```

## 📖 Next Steps

1. **Add Products** - Login as admin and add products
2. **Customize Branding** - Update logos, colors, text
3. **Add More Features** - Reviews, wishlist, recommendations
4. **Set Up Emails** - Order confirmations, notifications
5. **Deploy to Production** - Follow DEPLOYMENT.md

## 💡 Tips

- Use test data in development
- Test Stripe with their test card: 4242 4242 4242 4242
- Keep `.env` files out of version control
- Enable debug mode in development
- Use MongoDB Compass to view your database

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines

## 📞 Support

Need help? Check:
1. GitHub Issues - Report bugs
2. Discussions - Ask questions
3. Documentation - Read guides

## 🎯 What's Included

✅ Full-stack e-commerce boilerplate
✅ User authentication system
✅ Product catalog with search
✅ Shopping cart
✅ Order management
✅ Payment integration ready
✅ Admin capabilities
✅ Responsive design
✅ Deployment guides
✅ TypeScript support

## 🚀 Ready to Go Live?

Your app is production-ready! See [DEPLOYMENT.md](./DEPLOYMENT.md) for step-by-step deployment instructions.

---

**Let's build something amazing! 🎉**
