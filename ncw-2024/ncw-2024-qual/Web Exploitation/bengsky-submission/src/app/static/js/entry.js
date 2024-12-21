import('./profile.js')
  .then(module => {
    module.updateProfile();
  })
  .catch(err => {
    console.error('Failed to load module', err);
  });