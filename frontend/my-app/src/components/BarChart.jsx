// BarChart.js
import React from 'react';
import { Bar } from 'react-chartjs-2';
import 'chart.js/auto';

function BarChart({ data }) {
  const options = {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          color: '#000000',
          font: {
            size: 20, // Y-axis labels font size
          },
        },
      },
      x: {
        ticks: {
          color: '#000000',
          font: {
            size: 20, // X-axis labels font size
          },
        },
      },
    },
  };

  return (
    <div className='px-8 py-10'>
      <h1 className='text-2xl font-semibold'>Algorithm analysis</h1>
      <Bar data={data} options={options} />
    </div>
  );
}

export default BarChart;
