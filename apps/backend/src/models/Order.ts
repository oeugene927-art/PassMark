import mongoose, { Schema, Document } from 'mongoose';

export interface IOrderItem {
  productId: string;
  quantity: number;
  price: number;
}

export interface IOrder extends Document {
  userId: string;
  items: IOrderItem[];
  totalAmount: number;
  status: 'pending' | 'processing' | 'shipped' | 'delivered' | 'cancelled';
  shippingAddress: {
    street: string;
    city: string;
    state: string;
    zipCode: string;
    country: string;
  };
  paymentMethod: 'stripe' | 'paypal';
  paymentId?: string;
  trackingNumber?: string;
  notes?: string;
  createdAt: Date;
  updatedAt: Date;
}

const orderSchema = new Schema<IOrder>(
  {
    userId: {
      type: String,
      required: [true, 'User ID is required']
    },
    items: [
      {
        productId: String,
        quantity: Number,
        price: Number
      }
    ],
    totalAmount: {
      type: Number,
      required: [true, 'Total amount is required']
    },
    status: {
      type: String,
      enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'],
      default: 'pending'
    },
    shippingAddress: {
      street: String,
      city: String,
      state: String,
      zipCode: String,
      country: String
    },
    paymentMethod: {
      type: String,
      enum: ['stripe', 'paypal'],
      default: 'stripe'
    },
    paymentId: String,
    trackingNumber: String,
    notes: String
  },
  { timestamps: true }
);

export default mongoose.model<IOrder>('Order', orderSchema);
