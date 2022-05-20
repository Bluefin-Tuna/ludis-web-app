import React from 'react';
import Login from './components/Login';

const App: React.FC = () => {
  return (
    <body>
      <div className="verticalCenter" style={{ height: '100vh' }}>
        <Login />
      </div>
      <section style={{ height: '30vh', textAlign: 'center' }}>
        {/* <h1> Ludis</h1> */}
        <div className="info">
          <div className="grid-container">
            <div className="grid-item">
              <h1> About Ludis</h1>
              Ludis is a community of athletes. We build tools, spaces, and connections driven by self-expression.
              Our mission is to help everybody discover their own community.
            </div>
            <div className="grid-item">
              <h1> Join Us</h1>
              We put people first, and value craft and simplicity in our work.
              Our teams inspire creativity around the world, helping over 1 billion people create and share.
              Join us!
            </div>
            <div className="grid-item">
              <h1> Contact</h1>
              For press inquiries, please contact us via our newsroom
              <br /><br />
              For questions regarding products, submit a support request
              <br /><br />
              For questions regarding how we partner with brands, contact brands@ludis.com
            </div>
          </div>
        </div>
      </section>
    </body>
  )
}

export default App;
