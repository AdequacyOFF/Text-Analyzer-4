import React from 'react';
import {
  Chart as ChartJS,
  RadialLinearScale,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { PolarArea } from 'react-chartjs-2';

ChartJS.register(RadialLinearScale, ArcElement, Tooltip, Legend);

export function TextStyle(array) {
  console.log("TextStyle array: ", array);
  const data = {
  labels: ["Научный",
      "Публицистический",
      "Официально-деловой",
      "Художественный",
      "Разговорный"],
  datasets: [
    {
      label: "Article analysis for styles",
      data: [array["array"]["style_scientific_percent"],
          array["array"]["style_publicistic_percent"],
          array["array"]["style_official_percent"],
          array["array"]["style_artistic_percent"],
          array["array"]["style_conversational_percent"]],
      // data: [40, 70, 80, 13, 30],
      backgroundColor: [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
      ],
      borderWidth: 1,
    },
  ],
};

  return <PolarArea data={data} 
              width={400}
              height={400}
              options={{ maintainAspectRatio: false }}/>;
}