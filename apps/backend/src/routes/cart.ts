import express from 'express';
import { protect, AuthRequest } from '../middleware/auth.js';

const router = express.Router();
const carts = new Map();

// Get cart
router.get('/', protect, (req: AuthRequest, res) => {
  const cartData = carts.get(req.userId) || { items: [], total: 0 };
  res.json(cartData);
});

// Add to cart
router.post('/add', protect, (req: AuthRequest, res) => {
  try {
    const { productId, quantity, price } = req.body;
    let cart = carts.get(req.userId) || { items: [], total: 0 };
    
    const existingItem = cart.items.find((item: any) => item.productId === productId);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      cart.items.push({ productId, quantity, price });
    }
    
    cart.total = cart.items.reduce((sum: number, item: any) => sum + (item.price * item.quantity), 0);
    carts.set(req.userId, cart);
    
    res.json(cart);
  } catch (error) {
    res.status(400).json({ error: 'Failed to add to cart' });
  }
});

// Remove from cart
router.delete('/:productId', protect, (req: AuthRequest, res) => {
  try {
    let cart = carts.get(req.userId) || { items: [], total: 0 };
    cart.items = cart.items.filter((item: any) => item.productId !== req.params.productId);
    cart.total = cart.items.reduce((sum: number, item: any) => sum + (item.price * item.quantity), 0);
    carts.set(req.userId, cart);
    
    res.json(cart);
  } catch (error) {
    res.status(400).json({ error: 'Failed to remove from cart' });
  }
});

export default router;
