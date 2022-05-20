import React, { useReducer, useEffect, useCallback } from 'react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';

import TextField from '@material-ui/core/TextField';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import CardHeader from '@material-ui/core/CardHeader';
import Button from '@material-ui/core/Button';
import { FullscreenExit } from '@material-ui/icons';
import { Modal } from './Modal.component';

const logo = require('../logo.png');

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
    }
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

const Login = () => {
  const classes = useStyles();
  const [state, dispatch] = useReducer(reducer, initialState);

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

  const handleSignUp = () => {
    // this.props.history.push('./components/SignUp')
  }

  const [isModalOpen, setModalState] = React.useState(false);

  const toggleModal = () => setModalState(!isModalOpen);

  return (
    <form className={classes.container} noValidate autoComplete="off" style={{ display: 'flex' }}>
      {/* <Card className={classes.card}>
        <CardHeader className={classes.header} title="Login App" /> */}
      <div className="horizontalCenter">
        <img alt='logo' style={{ width: 100 }} src={String(logo)} />
      </div>
      <CardContent>
        <div>
          <TextField
            error={state.isError}
            fullWidth
            id="username"
            type="email"
            label="Username"
            placeholder="Username"
            margin="normal"
            onChange={handleUsernameChange}
            onKeyPress={handleKeyPress}
          />
          <TextField
            error={state.isError}
            fullWidth
            id="password"
            type="password"
            label="Password"
            placeholder="Password"
            margin="normal"
            helperText={state.helperText}
            onChange={handlePasswordChange}
            onKeyPress={handleKeyPress}
          />
        </div>
      </CardContent>
      <CardContent style={{ fontSize: 12 }}>
        <Button style={{ padding: 0, fontSize: 12, background: 'transparent', textTransform: 'none', textDecoration: 'none', color: 'gray' }} onClick={toggleModal} >
          Don't have an account? Sign up
        </Button>
        <div style={{ height: 30 }}></div>
        <a href="hardCodedSomething" >{"Forgot password"}</a>
      </CardContent>
      <CardActions style={{ marginLeft: "auto", paddingRight: "12%" }}>
        <Button
          variant="contained"
          size="large"
          color="secondary"
          className={classes.loginBtn}
          onClick={handleLogin}
          style={{ boxShadow: 'none', background: 'lightgrey', color: 'black' }}>
          Login
        </Button>
      </CardActions>
      {/* </Card> */}
      <Modal
        title={'Sign up'}
        isOpen={isModalOpen}
        onClose={toggleModal}
      >
        <CardContent>
          <div>
            <TextField
              error={state.isError}
              fullWidth
              id="username"
              type="email"
              label="First Name"
              placeholder="First Name"
              margin="normal"
              onChange={handleUsernameChange}
              onKeyPress={handleKeyPress}
            />
            <TextField
              error={state.isError}
              fullWidth
              id="username"
              type="email"
              label="Last Name"
              placeholder="Last Name"
              margin="normal"
              onChange={handleUsernameChange}
              onKeyPress={handleKeyPress}
            />
            <TextField
              error={state.isError}
              fullWidth
              id="password"
              type="password"
              label="Password"
              placeholder="Username"
              margin="normal"
              helperText={state.helperText}
              onChange={handlePasswordChange}
              onKeyPress={handleKeyPress}
            />
            <TextField
              error={state.isError}
              fullWidth
              id="password"
              type="password"
              label="Email"
              placeholder="Email"
              margin="normal"
              helperText={state.helperText}
              onChange={handlePasswordChange}
              onKeyPress={handleKeyPress}
            />
            <TextField
              error={state.isError}
              fullWidth
              id="password"
              type="password"
              label="Password"
              placeholder="Password"
              margin="normal"
              helperText={state.helperText}
              onChange={handlePasswordChange}
              onKeyPress={handleKeyPress}
            />
          </div>
          <div style={{ justifyContent: 'center', display: 'flex' }}>
            <Button
              style={{ background: 'lightgrey', marginTop: 30, padding: 10 }}
              onClick={history.push('./components/SignUp')}
            >
              Continue
            </Button>
          </div>
        </CardContent>
      </Modal>
    </form >
  );
}

export default Login;