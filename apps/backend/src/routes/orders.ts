import express from 'express';
import Order from '../models/Order.js';
import { protect, AuthRequest } from '../middleware/auth.js';

const router = express.Router();

// Create order
router.post('/', protect, async (req: AuthRequest, res) => {
  try {
    const { items, shippingAddress, paymentId } = req.body;
    
    const totalAmount = items.reduce((sum: number, item: any) => sum + (item.price * item.quantity), 0);
    
    const order = new Order({
      userId: req.userId,
      items,
      totalAmount,
      shippingAddress,
      paymentId,
      status: 'pending'
    });
    
    await order.save();
    res.status(201).json(order);
  } catch (error) {
    res.status(400).json({ error: 'Failed to create order' });
  }
});

// Get user orders
router.get('/', protect, async (req: AuthRequest, res) => {
  try {
    const orders = await Order.find({ userId: req.userId });
    res.json(orders);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch orders' });
  }
});

// Get order by ID
router.get('/:id', protect, async (req: AuthRequest, res) => {
  try {
    const order = await Order.findById(req.params.id);
    if (!order || order.userId !== req.userId) {
      return res.status(404).json({ error: 'Order not found' });
    }
    res.json(order);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch order' });
  }
});

export default router;
