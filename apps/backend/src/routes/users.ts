import express from 'express';
import User from '../models/User.js';
import { protect, AuthRequest } from '../middleware/auth.js';

const router = express.Router();

// Get profile
router.get('/profile', protect, async (req: AuthRequest, res) => {
  try {
    const user = await User.findById(req.userId).select('-password');
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch profile' });
  }
});

// Update profile
router.put('/profile', protect, async (req: AuthRequest, res) => {
  try {
    const user = await User.findByIdAndUpdate(req.userId, req.body, { new: true }).select('-password');
    res.json(user);
  } catch (error) {
    res.status(400).json({ error: 'Failed to update profile' });
  }
});

export default router;
