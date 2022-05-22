import '@fontsource/material-icons';
import 'materialize-css';
import '../scss/style.scss';

document.addEventListener('DOMContentLoaded', () => {
  const elems = document.querySelectorAll('.tooltipped');
  const instances = M.Tooltip.init(elems);
});
