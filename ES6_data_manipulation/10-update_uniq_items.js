export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  return map.forEach((val, key) => {
    if (val === 1) {
      map.set(key, 100);
    }
  });
}
