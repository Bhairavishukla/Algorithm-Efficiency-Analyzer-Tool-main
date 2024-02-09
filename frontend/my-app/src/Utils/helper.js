import { Store } from 'react-notifications-component';

function mapSortNames(names) {
  return names.map(
    (name) =>
      name
        .toLowerCase() // Convert the string to lowercase
        .replace(/\s+/g, '_') // Replace spaces with underscores
  );
}

function randomRGB() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `${r}, ${g}, ${b}`;
}

function giveWarningError(message) {
  return Store.addNotification({
    title: 'Warning',
    message: message,
    type: 'warning',
    insert: 'bottom',
    container: 'bottom-center',
    animationIn: ['animate__animated', 'animate__fadeIn'],
    animationOut: ['animate__animated', 'animate__fadeOut'],
    dismiss: {
      duration: 5000,
      onScreen: true,
    },
  });
}

function giveBadRequestError() {
  return Store.addNotification({
    title: 'Bad Request',
    message:
      'Kth Element Should be greater than zero and less than size of the array',
    type: 'danger',
    insert: 'center',
    container: 'center',
    animationIn: ['animate__animated', 'animate__fadeIn'],
    animationOut: ['animate__animated', 'animate__fadeOut'],
    dismiss: {
      duration: 5000,
      onScreen: true,
    },
  });
}

export { mapSortNames, randomRGB, giveBadRequestError, giveWarningError };
