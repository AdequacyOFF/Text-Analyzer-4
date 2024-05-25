import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export function Mychart(array) {
  console.log("Chart array: ", array);
  const data = {
  labels: ["Нейтральный",
      "Радость",
      "Печаль",
      "Удивление",
      "Страх",
      "Гнев"],
  datasets: [
    {
      label: "Text analysis based on emotions",
      data: [array["array"]["neutral_percent"],
          array["array"]["joy_percent"],
          array["array"]["sadness_percent"],
          array["array"]["surprise_percent"],
          array["array"]["fear_percent"],
          array["array"]["anger_percent"]],
      backgroundColor: [
        "rgb(173, 173, 173)",
          "rgb(245, 213, 63)",
          "rgb(99, 111, 189)",
          "rgb(8, 232, 222)",
          "rgb(134, 219, 74)",
          "rgb(222, 44, 44)"
      ],
      borderColor: [
        "rgba(173, 173, 173,0.7)",
          "rgba(245, 213, 63,0.7)",
          "rgba(99, 111, 189,0.7)",
          "rgba(8, 232, 222,0.7)",
          "rgba(134, 219, 74,0.5)",
          "rgba(222, 44, 44,0.5)"
      ],
      borderWidth: 1,
    },
  ],
};
  return <Doughnut data={data}
              options={{ 
                responsive: true,
                maintainAspectRatio: false 
              }}/>;
}
