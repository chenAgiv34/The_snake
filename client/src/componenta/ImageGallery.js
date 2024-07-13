import React, { useContext } from 'react';
import { ImageContext } from './ImageContext';
import { useNavigate } from 'react-router-dom';

const ImageGallery = () => {
  const { imageUrls } = useContext(ImageContext);
  const navigate = useNavigate();

  const handleGoBack = () => {
    navigate(-1); 
  };

  return (
    <>
    <button className= 'btn btn-primary' style={{backgroundColor: "darkseagreen",border: "black"}} onClick={handleGoBack}>Go Back</button>
    <div style={styles.gallery}>
      {imageUrls.map((image, index) => (
        <div key={index} style={styles.imageContainer}>
          <img src={image.url} alt={`Image ${index}`} style={styles.image} />
          <p>{image.parameter}</p>
        </div>
      ))}

    </div>
</>

  );
};

const styles = {
  gallery: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
  },
  imageContainer: {
    margin: '10px',
  },
  image: {
    width: '200px',
    height: '200px',
    objectFit: 'cover',
  },
};

export default ImageGallery;
