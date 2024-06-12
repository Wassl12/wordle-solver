import Box from '@mui/material/Box';
import './Box.css';

export default function BoxBasic() {
  return (
    <Box className='box' component="section" sx={{ p: 2, border: '2px solid grey' }}>
      <input className="input" maxLength={1}/>
    </Box>
  );
}