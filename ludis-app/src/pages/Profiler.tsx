import React, { useReducer, useEffect } from 'react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';

import TextField from '@material-ui/core/TextField';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import CardHeader from '@material-ui/core/CardHeader';
import Button from '@material-ui/core/Button';
import { Autorenew, FullscreenExit } from '@material-ui/icons';
import { Modal } from './Modal.component.tsx';
import { useNavigate } from 'react-router-dom';

export interface IProfilerPageProps { }

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
      width: 400,
      margin: `${theme.spacing(0)} auto`
    },
    loginBtn: {
      marginTop: theme.spacing(2),
      flexGrow: 1
    },
    header: {
      textAlign: 'center',
      background: '#212121',
      color: '#fff'
    },
    card: {
      marginTop: theme.spacing(10)
    },
  })
);

//state type

type State = {
  username: string
  password: string
  isButtonDisabled: boolean
  helperText: string
  isError: boolean
};

const initialState: State = {
  username: '',
  password: '',
  isButtonDisabled: true,
  helperText: '',
  isError: false
};

type Action = { type: 'setUsername', payload: string }
  | { type: 'setPassword', payload: string }
  | { type: 'setIsButtonDisabled', payload: boolean }
  | { type: 'loginSuccess', payload: string }
  | { type: 'loginFailed', payload: string }
  | { type: 'setIsError', payload: boolean };

const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case 'setUsername':
      return {
        ...state,
        username: action.payload
      };
    case 'setPassword':
      return {
        ...state,
        password: action.payload
      };
    case 'setIsButtonDisabled':
      return {
        ...state,
        isButtonDisabled: action.payload
      };
    case 'loginSuccess':
      return {
        ...state,
        helperText: action.payload,
        isError: false
      };
    case 'loginFailed':
      return {
        ...state,
        helperText: action.payload,
        isError: true
      };
    case 'setIsError':
      return {
        ...state,
        isError: action.payload
      };
  }
}

const ProfilerPage: React.FunctionComponent<IProfilerPageProps> = (props) => {
  const classes = useStyles();
  const [state, dispatch] = useReducer(reducer, initialState);
  const navigate = useNavigate();

  useEffect(() => {
    if (state.username.trim() && state.password.trim()) {
      dispatch({
        type: 'setIsButtonDisabled',
        payload: false
      });
    } else {
      dispatch({
        type: 'setIsButtonDisabled',
        payload: true
      });
    }
  }, [state.username, state.password]);

  const handleLogin = () => {
    if (state.username === 'abc@email.com' && state.password === 'password') {
      dispatch({
        type: 'loginSuccess',
        payload: 'Login Successfully'
      });
    } else {
      dispatch({
        type: 'loginFailed',
        payload: 'Incorrect username or password'
      });
    }
  };

  const handleKeyPress = (event: React.KeyboardEvent) => {
    if (event.keyCode === 13 || event.which === 13) {
      state.isButtonDisabled || handleLogin();
    }
  };

  const handleUsernameChange: React.ChangeEventHandler<HTMLInputElement> =
    (event) => {
      dispatch({
        type: 'setUsername',
        payload: event.target.value
      });
    };

  const handlePasswordChange: React.ChangeEventHandler<HTMLInputElement> =
    (event) => {
      dispatch({
        type: 'setPassword',
        payload: event.target.value
      });
    }

  const options = [
    'one', 'two', 'three'
  ];
  const defaultOption = options[0];

  return (
    <section>
      <div style={{
        margin: 'auto',
        width: 'auto',
        textAlign: 'center',
      }}>
        <h1 style={{ fontSize: 50 }}>Choose your <br /> sports preferences</h1>
      </div>
      <section style={{
        width: '35%',
        marginLeft: 'auto',
        marginRight: 'auto',
        marginBottom: 100,
      }}>
        <div>
          <h1>Outdoor Sports</h1>
          <select id='outdoorSports' style={{
            borderRadius: 20,
            width: 600,
            height: 50,
            fontSize: 20,
            textIndent: 10
          }}>
            <option value="Soccer">Soccer</option>
            <option value="Football">Football</option>
            <option value="Basketball">Basketball</option>
            <option value="Volleyball">Volleyball</option>
            <option value="Basketball">Basketball</option>
            <option value="Golf">Golf</option>
            <option value="Tennis">Tennis</option>
            <option value="Track">Track</option>
            <option value="Baseball">Baseball</option>
            <option value="Swimming">Swimming</option>
            <option value="Skateboarding">Skateboarding</option>
            <option value="Hiking">Hiking</option>
            <option value="Ultimate Frisbee">Ultimate Frisbee</option>
            <option value="Cross Country">Cross Country</option>
            <option value="Surfing">Surfing</option>
            <option value="Rock Climbing">Rock Climbing</option>
          </select>
        </div>
        <div>
          <h1>Indoor Sports</h1>
          <select id='indoorSports' style={{
            borderRadius: 20,
            width: 600,
            height: 50,
            fontSize: 20,
            textIndent: 10
          }}>
            <option value="Futsal">Futsal</option>
            <option value="Bowling">Bowling</option>
            <option value="Table Tennis">Table Tennis</option>
            <option value="Badminton">Badminton</option>
            <option value="Hockey">Hockey</option>
            <option value="Ice Skating">Ice Skating</option>
            <option value="Gymnastics">Gymnastics</option>
            <option value="Weight Training">Weight Training</option>
            <option value="Billiards">Billiards</option>
            <option value="Darts">Darts</option>
          </select>
        </div>
        <div>
          <h1>Other</h1>
          <select id='indoorSports' style={{
            borderRadius: 20,
            width: 600,
            height: 50,
            fontSize: 20,
            textIndent: 10
          }}>
            <option value="Futsal">Futsal</option>
            <option value="Bowling">Bowling</option>
            <option value="Table Tennis">Table Tennis</option>
            <option value="Badminton">Badminton</option>
            <option value="Hockey">Hockey</option>
          </select>
        </div>
        <div>
          <h1>Rating</h1>
          <select id='indoorSports' style={{
            borderRadius: 20,
            width: 600,
            height: 50,
            fontSize: 20,
            textIndent: 10
          }}>
            <option value="One">One</option>
            <option value="Two">Two</option>
            <option value="Three">Three</option>
            <option value="Four">Four</option>
            <option value="Five">Five</option>
          </select>
        </div>
        <div style={{
          justifyContent: 'center',
          display: 'flex',
          marginTop: 50
        }}
        >
          <Button
            style={{
              background: 'lightgrey',
              marginTop: 40,
              padding: 20,
              width: 250,
              fontSize: 20,
              borderRadius: 20
            }}
            onClick={() => navigate('/')}
          >
            Continue
          </Button>
        </div>
      </section>
    </section >
  );
}

export default ProfilerPage;