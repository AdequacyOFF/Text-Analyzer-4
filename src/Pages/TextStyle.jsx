import React from 'react';
import { Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from 'chart.js';
import { Radar } from 'react-chartjs-2';

ChartJS.register(RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend);

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
      data: [array["array"]["style_scientific_percent"] * 100,
          array["array"]["style_publicistic_percent"] * 100,
          array["array"]["style_official_percent"] * 100,
          array["array"]["style_artistic_percent"] * 100,
          array["array"]["style_conversational_percent"] * 100],
      // data: [40, 70, 80, 13, 30],
      backgroundColor: ["rgba(75,192,192,0.4)"],
      borderColor: ["rgba(75,192,192,0.4)"],
      borderWidth: 1,
    },
  ],
};

  return <Radar data={data} 
              width={400}
              height={400}
              options={{ maintainAspectRatio: false }}/>;
}