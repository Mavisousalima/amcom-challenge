import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface ProductData {
  id: number;
  code: string;
  description: string;
}

const Product = () => {
  const [products, setProducts] = useState<ProductData[]>([]);
  const [search, setSearch] = useState<string>('');
  
  useEffect(() => {
    axios.get('http://localhost:8000/api/products/')
      .then(response => setProducts(response.data))
      .catch(error => console.error(error));
  }, []);

  const filteredProducts = products.filter(product => {
    return (
      product.description.toLowerCase().includes(search.toLowerCase()) ||
      product.code.toLowerCase().includes(search.toLowerCase())
    );
  });

  return (
    <div>
      <h2>Product Component</h2>
      <input
        type="text"
        placeholder="Search by code or description"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      {filteredProducts.map(product => (
        <div key={product.id}>
          <p>Description: {product.description}</p>
          <p>Code: {product.code}</p>
        </div>
      ))}
    </div>
  );
}

export default Product;