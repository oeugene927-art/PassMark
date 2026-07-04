'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useAppDispatch } from '@/store/hooks';
import { addToCart } from '@/store/slices/cartSlice';

interface ProductCardProps {
  _id: string;
  name: string;
  price: number;
  images: string[];
  rating: number;
  description: string;
}

export function ProductCard({ _id, name, price, images, rating, description }: ProductCardProps) {
  const dispatch = useAppDispatch();
  const [quantity, setQuantity] = useState(1);

  const handleAddToCart = () => {
    dispatch(addToCart({
      productId: _id,
      quantity,
      price,
      name,
    }));
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      <div className="relative h-48 bg-gray-200">
        {images && images[0] ? (
          <img
            src={images[0]}
            alt={name}
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-gray-400">
            No Image
          </div>
        )}
      </div>
      
      <div className="p-4">
        <Link href={`/products/${_id}`}>
          <h3 className="font-bold text-lg hover:text-primary cursor-pointer">{name}</h3>
        </Link>
        
        <p className="text-gray-600 text-sm mb-2 line-clamp-2">{description}</p>
        
        <div className="flex items-center justify-between mb-4">
          <span className="text-2xl font-bold text-primary">${price}</span>
          <span className="text-yellow-500">★ {rating}</span>
        </div>
        
        <div className="flex gap-2">
          <input
            type="number"
            min="1"
            value={quantity}
            onChange={(e) => setQuantity(parseInt(e.target.value))}
            className="w-12 px-2 py-1 border rounded"
          />
          <button
            onClick={handleAddToCart}
            className="flex-1 bg-primary text-white px-4 py-2 rounded hover:bg-secondary transition"
          >
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}
