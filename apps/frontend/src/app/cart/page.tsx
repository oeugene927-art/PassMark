'use client';

import { useAppSelector, useAppDispatch } from '@/store/hooks';
import { removeFromCart, clearCart } from '@/store/slices/cartSlice';
import Link from 'next/link';

export default function CartPage() {
  const dispatch = useAppDispatch();
  const { items, total } = useAppSelector(state => state.cart);

  if (items.length === 0) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8">Shopping Cart</h1>
        <div className="text-center py-12">
          <p className="text-gray-500 mb-4">Your cart is empty</p>
          <Link
            href="/products"
            className="bg-primary text-white px-6 py-2 rounded hover:bg-secondary"
          >
            Continue Shopping
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">Shopping Cart</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <div className="bg-white rounded-lg shadow">
            {items.map(item => (
              <div key={item.productId} className="border-b p-4 flex justify-between items-center">
                <div>
                  <h3 className="font-bold">{item.name}</h3>
                  <p className="text-gray-600">Quantity: {item.quantity}</p>
                  <p className="text-primary font-bold">${(item.price * item.quantity).toFixed(2)}</p>
                </div>
                <button
                  onClick={() => dispatch(removeFromCart(item.productId))}
                  className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6 h-fit">
          <h2 className="text-2xl font-bold mb-4">Order Summary</h2>
          <div className="mb-4">
            <div className="flex justify-between mb-2">
              <span>Subtotal:</span>
              <span>${total.toFixed(2)}</span>
            </div>
            <div className="flex justify-between mb-2">
              <span>Shipping:</span>
              <span>$0.00</span>
            </div>
            <div className="flex justify-between mb-4 text-lg font-bold border-t pt-4">
              <span>Total:</span>
              <span>${total.toFixed(2)}</span>
            </div>
          </div>
          
          <Link
            href="/checkout"
            className="w-full bg-primary text-white px-4 py-2 rounded hover:bg-secondary text-center block"
          >
            Proceed to Checkout
          </Link>
          
          <button
            onClick={() => dispatch(clearCart())}
            className="w-full mt-2 bg-gray-200 text-gray-800 px-4 py-2 rounded hover:bg-gray-300"
          >
            Clear Cart
          </button>
        </div>
      </div>
    </div>
  );
}
