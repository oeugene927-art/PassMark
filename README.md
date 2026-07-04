# PassMark E-Commerce Platform

🚀 **A production-ready full-stack e-commerce platform**

![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)
![Node](https://img.shields.io/badge/node-18%2B-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## ⚡ Quick Links

- 📖 [Quick Start Guide](./QUICKSTART.md)
- 🚀 [Deployment Guide](./DEPLOYMENT.md)
- 🤝 [Contributing Guide](./CONTRIBUTING.md)
- 📚 [API Documentation](./docs/API.md) (Coming soon)

## 🌟 Features

### For Customers
- 🛍️ Browse and search products
- 🛒 Add to cart and wishlist
- 💳 Secure checkout with Stripe
- 👤 User accounts and order history
- ⭐ Product reviews and ratings
- 📱 Fully responsive design
- 🔐 Secure authentication

### For Admins
- 📊 Dashboard with analytics
- 📦 Inventory management
- 👥 Customer management
- 📈 Sales reports
- 🎨 Product management
- 💰 Payment processing

## 🏗️ Architecture

```
┌─────────────────────┐
│   Next.js Frontend  │ (Vercel)
│  React + Redux      │
│  Tailwind CSS       │
└──────────┬──────────┘
           │ HTTP/REST
           ▼
┌─────────────────────┐
│  Express Backend    │ (Railway/Render)
│  Node.js + MongoDB  │
│  JWT + Stripe       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  MongoDB Atlas      │
│  (Database)         │
└─────────────────────┘
```

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/oeugene927-art/PassMark.git
cd PassMark
npm install
```

### 2. Setup Environment
```bash
cp apps/backend/.env.example apps/backend/.env
# Edit .env with your MongoDB and Stripe keys
```

### 3. Run Development Servers
```bash
npm run dev
```

- Frontend: http://localhost:3000
- Backend: http://localhost:5000

**For detailed setup instructions, see [QUICKSTART.md](./QUICKSTART.md)**

## 📁 Project Structure

```
PassMark/
├── apps/
│   ├── backend/              # Node.js/Express API
│   │   ├── src/
│   │   │   ├── routes/       # API endpoints
│   │   │   ├── models/       # MongoDB schemas
│   │   │   ├── middleware/   # Auth & utilities
│   │   │   └── server.ts     # Entry point
│   │   ├── package.json
│   │   └── .env.example
│   │
│   └── frontend/             # Next.js React app
│       ├── src/
│       │   ├── app/          # Pages
│       │   ├── components/   # Components
│       │   ├── store/        # Redux store
│       │   └── lib/          # API client
│       ├── package.json
│       └── next.config.js
│
├── docs/                     # Documentation
├── QUICKSTART.md             # Setup guide
├── DEPLOYMENT.md             # Deploy to production
├── CONTRIBUTING.md           # Contributing
└── package.json
```

## 🔌 API Endpoints

### Auth
```
POST   /api/auth/register
POST   /api/auth/login
```

### Products
```
GET    /api/products
GET    /api/products/:id
POST   /api/products          (admin)
PUT    /api/products/:id      (admin)
DELETE /api/products/:id      (admin)
```

### Cart
```
GET    /api/cart
POST   /api/cart/add
DELETE /api/cart/:productId
```

### Orders
```
POST   /api/orders
GET    /api/orders
GET    /api/orders/:id
```

### Users
```
GET    /api/users/profile
PUT    /api/users/profile
```

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14, React 18, TypeScript |
| Styling | Tailwind CSS |
| State | Redux Toolkit |
| Backend | Node.js, Express.js |
| Database | MongoDB, Mongoose |
| Auth | JWT |
| Payments | Stripe |
| Deployment | Vercel, Railway |

## 📦 Getting to Production

### Frontend Deployment (Vercel)
1. Push code to GitHub
2. Connect repo to Vercel
3. Set environment variables
4. Deploy! ✨

### Backend Deployment (Railway)
1. Connect GitHub repo to Railway
2. Add environment variables
3. Deploy! ✨

### Database (MongoDB Atlas)
1. Create free tier cluster
2. Get connection string
3. Add to backend `.env`

**See [DEPLOYMENT.md](./DEPLOYMENT.md) for full instructions**

## 🧪 Test Stripe Locally

Use these test card numbers:
- **Success**: 4242 4242 4242 4242
- **Failure**: 4000 0000 0000 0002

## 🔒 Security

✅ JWT authentication
✅ Password hashing (bcrypt)
✅ CORS protection
✅ Rate limiting
✅ SQL injection prevention
✅ XSS protection
✅ Environment variables
✅ Secure headers

## 📊 Performance

- ⚡ Next.js optimizations
- 🖼️ Image optimization
- 💾 Redis caching ready
- 📦 Gzip compression
- 🚀 CDN support

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](./LICENSE) file

## 🚀 Roadmap

- [ ] Admin dashboard
- [ ] Advanced search filters
- [ ] Product recommendations
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Mobile app (React Native)
- [ ] AI chatbot support
- [ ] Multi-language support
- [ ] Multi-currency support
- [ ] Subscription products

## 💬 Support

- 📧 Email: support@passmark.app
- 🐛 [Issues](https://github.com/oeugene927-art/PassMark/issues)
- 💬 [Discussions](https://github.com/oeugene927-art/PassMark/discussions)

## 🙏 Acknowledgments

- Built with ❤️ for the open-source community
- Powered by amazing tools and frameworks
- Thanks to all contributors

---

**Ready to launch your e-commerce store?** 🎉

[Get Started Now →](./QUICKSTART.md)
