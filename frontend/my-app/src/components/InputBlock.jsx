function InputBlock({ onChangeHandler, value, className, children, type }) {
  return (
    <div className={className}>
      <label
        className='block text-sm font-bold mb-2  uppercase text-stone-700'
        htmlFor='unsorted-array'>
        {children}
      </label>
      <input
        className='shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
        id='unsorted-array'
        type={type}
        value={value}
        onChange={onChangeHandler}
      />
    </div>
  );
}

export default InputBlock;
