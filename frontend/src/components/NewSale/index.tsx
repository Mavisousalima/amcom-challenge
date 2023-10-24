import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ReactSearchAutocomplete } from 'react-search-autocomplete';
import { Link } from 'react-router-dom';
import './styles.css';
import TrashCan from './trash-can.svg';

interface ProductData {
    id: number,
    code: string,
    description: string,
    unit_price: number,
    quantity: number,
    total: number
}

interface SellerData {
    id: number,
    name: string,
    email: string,
    phone: string
}

interface ClientData {
    id: number,
    name: string,
    email: string,
    phone: string
}

function NewSale() {
    const [products, setProducts] = useState<ProductData[]>([]);
    const [selectedProduct, setSelectedProduct] = useState<ProductData | null>(null);
    const [quantity, setQuantity] = useState(0);
    const [selectedProducts, setSelectedProducts] = useState<ProductData[]>([]);
    const [sellers, setSellers] = useState<SellerData[]>([]);
    const [selectedSellerId, setSelectedSellerId] = useState<SellerData>();
    const [clients, setClients] = useState<ClientData[]>([]);
    const [currentDate, setCurrentDate] = useState<string>(getCurrentDate());
    
    useEffect(() => {
      axios.get('http://localhost:8000/api/products/')
        .then(response => setProducts(response.data))
        .catch(error => console.error(error));
    }, []);

    useEffect(() => {
        axios.get('http://localhost:8000/api/sellers/')
          .then(response => setSellers(response.data))
          .catch(error => console.error(error));
      }, []);

      useEffect(() => {
        axios.get('http://localhost:8000/api/clients/')
          .then(response => setClients(response.data))
          .catch(error => console.error(error));
      }, []);

    const items = products.map((product) => ({
        id: product.id,
        code: product.code,
        name: product.description
      }));

  const handleOnSearch = (string: String, results: any) => {
    console.log(string, results)
  }

  const handleOnSelect = (product: any) => {
    const selected = products.find((p) => p.id === product.id);
    setSelectedProduct(selected || null);
  };

  const handleAddProduct = () => {
    if (selectedProduct) {
      const total = selectedProduct.unit_price * quantity;
      const productToAdd = { ...selectedProduct, quantity, total };
      setSelectedProducts([...selectedProducts, productToAdd]);
      setSelectedProduct(null);
      setQuantity(0);
    }
  };

  const handleRemoveProduct = (productId: number) => {
    const updatedProducts = selectedProducts.filter((product) => product.id !== productId);
    setSelectedProducts(updatedProducts);
  };

  const handleSellerChange = (event: any) => {
    setSelectedSellerId(event.target.value);
  };

  const handleClientChange = (event: any) => {
    setSelectedSellerId(event.target.value);
  };

  const formatResult = (product: any) => {
    return (
      <>
        <span style={{ display: 'block', textAlign: 'left' }}>{product.code} - {product.name}</span>
      </>
    )
  }

  function getCurrentDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');

    return `${day}/${month}/${year} ${hours}:${minutes}`;
  }

  return (
    <div className='container'>
        <div className='d-flex'>
            <div style={{padding: '10px'}}>
                <div>
                    <h2>Produtos</h2>
                    <div className='d-flex justify-content-space-between'>
                        <div style={{ width: 400, marginRight: '20px' }}>
                            <label htmlFor="product-search">Buscar pelo código de barras ou descrição</label>
                            <ReactSearchAutocomplete
                                items={items}
                                onSearch={handleOnSearch}
                                onSelect={handleOnSelect}
                                autoFocus
                                formatResult={formatResult}
                                showIcon={false}
                                placeholder='Digite o código ou nome do produto'
                                className='search-auto-complete'
                            />
                        </div>
                        <div className='d-flex justify-content-space-between'>
                            <div style={{marginRight: '10px'}}>
                                <label htmlFor="product-quantity" style={{display: 'block'}}>Quantidade de itens</label>
                                <div className='d-flex'>
                                    <input 
                                        id='product-quantity'
                                        value={quantity}
                                        onChange={(e) => setQuantity(Number(e.target.value))}
                                        style={{border: '0.5px solid #C4C4C4', borderRadius: '3px', color: '#888888', padding: '10px', marginRight: '10px'}}
                                        >
                                    </input>
                                    <button className='btn btn-success' onClick={handleAddProduct}>Adicionar </button>
                                </div>
                            </div>
                            <div>
                             
                            </div>
                        </div>
                    </div>
                </div>
                <div style={{marginTop: '72px'}}>
                    <table style={{width: '100%', textAlign: 'left'}}>
                        <thead>
                            <tr>
                                <th>Produtos/Serviços</th>
                                <th>Quantidade</th>
                                <th>Preço unitário</th>
                                <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                        {selectedProducts.map((product) => (
                            <tr key={product.id}>
                                <td>{product.description}</td>
                                <td>{product.quantity}</td>
                                <td>R$ {product.unit_price}</td>
                                <td>R$ {product.total}</td>
                                <td>
                                    <button
                                    onClick={() => handleRemoveProduct(product.id)}
                                    style={{backgroundColor: 'transparent'}}
                                    >
                                    <i><img src={TrashCan} alt="" /></i>
                                    </button>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
            </div>
            <div style={{width: '100%', padding: '10px'}}>
                <h2>Dados da venda</h2>
                <label htmlFor="date-hour-sale" style={{display: 'block'}}>Data e Hora da Venda</label>
                <input
                    id="date-hour-sale"
                    type="text"
                    value={currentDate} // Set the initial date value
                    onChange={(e) => setCurrentDate(e.target.value)} // Allow editing
                    style={{ width: '-webkit-fill-available' }}
                />

                <label htmlFor="choose-seller" style={{display: 'block', marginTop: '27px'}}>Escolha um vendedor</label>
                <select
                    id="choose-seller"
                    onChange={handleSellerChange}
                    style={{ width: '-webkit-fill-available' }}
                    >
                    <option value="">Selecione um vendedor</option>
                    {sellers.map(seller => (
                        <option key={seller.id} value={seller.id}>
                        {seller.name}
                        </option>
                    ))}
                </select>

                <label htmlFor="choose-client" style={{display: 'block', marginTop: '27px'}}>Escolha um cliente</label>
                <select
                    id="choose-client"
                    onChange={handleSellerChange}
                    style={{ width: '-webkit-fill-available' }}
                    >
                    <option value="">Selecione um cliente</option>
                    {clients.map(client => (
                        <option key={client.id} value={client.id}>
                        {client.name}
                        </option>
                    ))}
                </select>

                <p style={{marginTop: '27px'}}>Valor total da venda: </p>

                <div className='d-flex justify-content-space-between'>
                    <Link to="/"><button className='btn btn-success'>Cancelar</button></Link>
                    <button className='btn btn-success'>Finalizar</button>
                </div>
            </div>
        </div>
    </div>
  )
}

export default NewSale