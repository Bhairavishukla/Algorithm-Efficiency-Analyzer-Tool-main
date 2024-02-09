import { useState } from 'react';
import BarChart from './components/BarChart';

import { ReactNotifications } from 'react-notifications-component';
import background from './assets/background.png';
import 'react-notifications-component/dist/theme.css';

import {
  mapSortNames,
  giveWarningError,
  giveBadRequestError,
  randomRGB,
} from './Utils/helper';
import { useRef } from 'react';
import axios from 'axios';

import './App.css';
import Header from './components/Header';
import InputBlock from './components/InputBlock';

function App() {
  const options = [
    'Merge Sort',
    'Quick Sort',
    'Insertion Sort',
    'Bubble Sort',
    'Heap Sort',
    'Bucket Sort',
    'Radix Sort',
    'Selection Sort',
    'Counting Sort',
    'Quick Select',
  ];
  //Bubble Sort

  // State to keep track of selected options
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [quickSelectValue, setQuickSelectValue] = useState(null);

  const [userInput, setUserInput] = useState([]);
  const [arraySize, setArraySize] = useState(0);

  const [chartData, setChartData] = useState({});

  const [showGraph, setShowGraph] = useState(false);

  const [loading, setLoading] = useState(false);
  const animationInterval = useRef(null);

  const handleChange = (event) => {
    const selectedOption = event.target.value;

    // Remove the option if it's already selected
    if (selectedOptions.includes(selectedOption)) {
      setSelectedOptions((prev) =>
        prev.filter((option) => option !== selectedOption)
      );

      if (selectedOption === 'Quick Select') {
        setQuickSelectValue(null); // Reset Quick Select value
      }
      return; // Early return to prevent further execution
    }

    // Prompt for a value only if 'Quick Select' is selected and not already in the list
    if (selectedOption === 'Quick Select') {
      const userInput = prompt(
        'Please enter a numerical value for Quick Select:'
      );

      // Check if user cancelled the prompt
      if (userInput === null) {
        return; // Do not add 'Quick Select' if the user cancelled the prompt
      }

      const numericalValue = parseInt(userInput, 10);
      if (!isNaN(numericalValue)) {
        setQuickSelectValue(numericalValue);
      } else {
        alert('Please enter a valid number');
        return; // Early return to prevent adding 'Quick Select' if no valid number is entered
      }
    }

    // Add the selected option
    setSelectedOptions((prev) => [...prev, selectedOption]);
  };

  function handleUserInputChange(event) {
    setUserInput(event.target.value.split(',').map((item) => item.trim()));
  }

  function handleSizeChange(event) {
    setArraySize(event.target.value);
  }

  function generateRandomArray() {
    const randomArray = Array.from({ length: arraySize }, () =>
      Math.floor(Math.random() * 10000)
    );
    setUserInput(randomArray);
  }

  async function handlePerformAnalysis(inputArray, selectedAlgorithm) {
    //setShowGraph(false);
    if (inputArray.length > 1 && selectedAlgorithm.length > 0) {
      const requestData = {
        array: inputArray,
        algorithms: mapSortNames(selectedAlgorithm),
        k: quickSelectValue,
      };
      setLoading(true);
      setChartData(createPlaceholderData());
      animationInterval.current = setInterval(
        () => updatePlaceholderData(),
        500
      );
      setShowGraph(true);
      console.log(requestData);

      try {
        const response = await axios.post(
          'https://algorithm-analyzer-backend.onrender.com/sort/',
          requestData
        );
        //const response = responseData;
        const algorithmDataPlot = response.data;

        console.log(algorithmDataPlot);

        const data = {
          labels: algorithmDataPlot.map((algo) => algo.name),
          datasets: [
            {
              label: 'Time Taken (ms)',
              data: algorithmDataPlot.map((algo) => algo.timeTaken),
              backgroundColor: algorithmDataPlot.map(
                () => `rgba(${randomRGB()},0.6)`
              ),
              borderColor: algorithmDataPlot.map(
                () => `rgba(${randomRGB()}, 1)`
              ),
              borderWidth: 1,
            },
          ],
        };

        //console.log(data.datasets);
        clearInterval(animationInterval.current);
        setChartData(data);
      } catch (error) {
        console.error('Error fetching data: ', error);
        clearInterval(animationInterval.current);
        setShowGraph(false);
        giveBadRequestError();
      } finally {
        setLoading(false);
      }
    } else {
      setShowGraph(false);
      if (inputArray.length === 0 && selectedAlgorithm.length === 0) {
        giveWarningError(
          'Please Enter Array values and Select a Algorithm to run the analysis'
        );
      } else {
        if (inputArray.length === 0) {
          giveWarningError('Please enter values in unsorted array');
        }
        if (selectedAlgorithm.length === 0) {
          giveWarningError('Please select atleast one algorithm');
        }
      }
    }
  }

  //graph animation

  const createPlaceholderData = () => {
    const length = selectedOptions.length;
    console.log(selectedOptions);
    return {
      labels: selectedOptions.map((algo) => algo),
      datasets: [
        {
          label: 'Time Taken (ms)',
          data: Array.from({ length }, () => Math.random() * 100),
          backgroundColor: 'rgba(0, 123, 255, 0.5)',
          borderColor: 'rgba(0, 123, 255, 1)',
          borderWidth: 1,
        },
      ],
    };
  };

  const updatePlaceholderData = () => {
    const length = selectedOptions.length;
    setChartData((oldData) => ({
      ...oldData,
      datasets: [
        {
          ...oldData.datasets[0],
          data: Array.from({ length }, () => Math.random() * 100),
        },
      ],
    }));
  };

  return (
    <div
      className='container mx-auto px-8 py-2 text-center'
      style={{
        background: `url(${background})`,
        backgroundSize: `cover`,
      }}>
      <ReactNotifications />
      <Header />
      <div className='grid grid-cols-1 md:grid-cols-2 gap-4 mb-4 mt-8'>
        <InputBlock
          onChangeHandler={handleUserInputChange}
          value={userInput}
          type={'text'}>
          Enter Unsorted Array
        </InputBlock>

        <div className='flex align-items-center'>
          <InputBlock
            onChangeHandler={handleSizeChange}
            value={arraySize}
            className={'flex-grow'}
            type={'number'}>
            Enter Size of the Array
          </InputBlock>

          <button
            className='ml-4  bg-stone-700 text-stone-400 hover:bg-stone-600 hover:text-stone-100  font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline'
            onClick={generateRandomArray}>
            Generate Array
          </button>
        </div>
      </div>

      <p className='block text-gray-700 text-sm font-bold mb-2'>
        Select the algorithms to compare
      </p>
      <div className='flex justify-between flex-wrap gap-4 mb-4 '>
        {options.map((option, index) => (
          <label key={index} className='inline-flex items-center'>
            <input
              className='form-checkbox h-5 w-5 text-gray-600'
              type='checkbox'
              value={option}
              checked={selectedOptions.includes(option)}
              onChange={handleChange}
            />
            <span className='ml-2 text-gray-700'>{option}</span>
          </label>
        ))}
      </div>

      <button
        disabled={loading}
        className=' bg-stone-700 text-stone-400 hover:bg-stone-600 hover:text-stone-100 font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full'
        onClick={() => handlePerformAnalysis(userInput, selectedOptions)}>
        Perform Analysis
      </button>

      {showGraph ? <BarChart className='p-4 m-4' data={chartData} /> : null}
    </div>
  );
}

export default App;
