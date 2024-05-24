import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Radar } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

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
      data: [array["array"]["stylel_scientific_percent"],
          array["array"]["style_publicistic_percent"],
          array["array"]["stylel_official_percent"],
          array["array"]["stylel_artistic_percent"],
          array["array"]["stylel_conversational_percent"]],
      // data: [40, 70, 80, 13, 30],
      backgroundColor: ["rgba(75,192,192,0.4)"],
      borderWidth: 1,
    },
  ],
};

  return <Radar data={data} 
              width={200}
              height={200}
              options={{ maintainAspectRatio: false }}/>;
}