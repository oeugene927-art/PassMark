import express from 'express';
import Product from '../models/Product.js';
import { protect, isAdmin } from '../middleware/auth.js';

const router = express.Router();

// Get all products
router.get('/', async (req, res) => {
  try {
    const { category, minPrice, maxPrice, search } = req.query;
    let query: any = { isActive: true };

    if (category) query.category = category;
    if (minPrice || maxPrice) {
      query.price = {};
      if (minPrice) query.price.$gte = Number(minPrice);
      if (maxPrice) query.price.$lte = Number(maxPrice);
    }
    if (search) {
      query.$or = [
        { name: { $regex: search, $options: 'i' } },
        { description: { $regex: search, $options: 'i' } }
      ];
    }

    const products = await Product.find(query).limit(100);
    res.json(products);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch products' });
  }
});

// Get single product
router.get('/:id', async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) return res.status(404).json({ error: 'Product not found' });
    res.json(product);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch product' });
  }
});

// Create product (admin only)
router.post('/', protect, async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.status(201).json(product);
  } catch (error) {
    res.status(400).json({ error: 'Failed to create product' });
  }
});

// Update product (admin only)
router.put('/:id', protect, async (req, res) => {
  try {
    const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(product);
  } catch (error) {
    res.status(400).json({ error: 'Failed to update product' });
  }
});

// Delete product (admin only)
router.delete('/:id', protect, async (req, res) => {
  try {
    await Product.findByIdAndDelete(req.params.id);
    res.json({ message: 'Product deleted' });
  } catch (error) {
    res.status(400).json({ error: 'Failed to delete product' });
  }
});

export default router;
