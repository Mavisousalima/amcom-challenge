import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './styles.css';

interface ProductData {
    description: string
}

interface ClientData {
    name: string
}

interface SellerData {
    name: string
}

interface SaleData {
    id: number,
    invoice_number: string,
    date_time: Date,
    client: ClientData
    seller: SellerData,
    products: [
        ProductData
    ]
}

const SalesTable = () => {
  const [sales, setSales] = useState<SaleData[]>([]);
  const [expandedSale, setExpandedSale] = useState<number | null>(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/sales/')
      .then(response => setSales(response.data))
      .catch(error => console.error(error));
  }, []);

  const toggleExpand = (saleId: number) => {
    if (expandedSale === saleId) {
      setExpandedSale(null);
    } else {
      setExpandedSale(saleId);
    }
  };

  return (
    <div style={{padding: '10px'}}>
        <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
            <h1 style={{color: '#00585E'}}>Vendas Realizadas</h1>
            <div>
            <Link to="/new-sale" style={{backgroundColor: '#00585E', color: '#ffffff', padding: '10px'}}>Inserir nova Venda</Link>
            </div>
        </div>
        <table style={{width: '100%', textAlign: 'left'}}>
            <thead>
                <tr>
                    <th>Nota Fiscal</th>
                    <th>Cliente</th>
                    <th>Vendedor</th>
                    <th>Data de Venda</th>
                    <th>Valor Total</th>
                    <th>Opções</th>
                </tr>
            </thead>
            <tbody>
                {sales.map(sale => (
                <tr key={sale.id}>
                    <td>{sale.invoice_number}</td>
                    <td>{sale.client.name}</td>
                    <td>{sale.seller.name}</td>
                    <td>{new Date(sale.date_time).toLocaleString()}</td>
                    <td>
                    <button onClick={() => toggleExpand(sale.id)} style={{backgroundColor: 'transparent', color: '#00585E'}}>
                        {expandedSale === sale.id ? 'Ocultar Itens' : 'Ver Itens'}
                    </button>
                    <button>Edit</button>
                    <button>Delete</button>
                    </td>
                </tr>
                ))}
            </tbody>
        </table>
    </div>
  );
};

export default SalesTable;
