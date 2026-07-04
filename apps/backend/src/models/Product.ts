import mongoose, { Schema, Document } from 'mongoose';

export interface IProduct extends Document {
  name: string;
  description: string;
  price: number;
  originalPrice?: number;
  stock: number;
  category: string;
  images: string[];
  rating: number;
  reviews: string[];
  sku: string;
  tags: string[];
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}

const productSchema = new Schema<IProduct>(
  {
    name: {
      type: String,
      required: [true, 'Product name is required'],
      trim: true
    },
    description: {
      type: String,
      required: [true, 'Product description is required']
    },
    price: {
      type: Number,
      required: [true, 'Product price is required'],
      min: [0, 'Price cannot be negative']
    },
    originalPrice: Number,
    stock: {
      type: Number,
      required: [true, 'Stock is required'],
      default: 0
    },
    category: {
      type: String,
      required: [true, 'Category is required']
    },
    images: {
      type: [String],
      required: [true, 'At least one image is required']
    },
    rating: {
      type: Number,
      default: 0,
      min: 0,
      max: 5
    },
    reviews: [String],
    sku: {
      type: String,
      required: true,
      unique: true
    },
    tags: [String],
    isActive: {
      type: Boolean,
      default: true
    }
  },
  { timestamps: true }
);

export default mongoose.model<IProduct>('Product', productSchema);
