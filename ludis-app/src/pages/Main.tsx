import React from 'react';

export interface IMainPageProps { }

const MainPage: React.FunctionComponent<IMainPageProps> = (props) => {
  return (
    <div>
      <p>This is the main page.</p>
    </div>
  )
}

export default MainPage;