import logoImg from '../assets/Logo-clearbg.png';
function Header() {
  return (
    <>
      <img
        className='w-[10rem] h-[10rem] items-center inline-flex '
        src={logoImg}
        alt=''
      />
      <h1 className='text-4xl font-bold text-center mb-6'>
        Algorithm Efficiency Analyzer Tool
      </h1>
    </>
  );
}

export default Header;
