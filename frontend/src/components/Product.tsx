import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface ProductData {
  id: number;
  description: string;
}

const Product = () => {
  const [products, setProducts] = useState<ProductData[]>([]);
  
  useEffect(() => {
    axios.get('http://localhost:8000/api/products/')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Product Component</h2>
      {products.map(product => (
        <div key={product.id}>
          <p>Description: {product.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Product;