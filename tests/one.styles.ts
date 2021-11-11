import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.grey['100'],
    borderRadius: '8px',
    color: theme.palette.grey.A300,
    textAlign: 'center',
    fontSize: '1rem',
    padding: '1.25rem 1.5rem',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    flexDirection: 'row',
    overflow: 'hidden',
    position: 'relative',
    [theme.breakpoints.down('md')]: {
      flexDirection: 'column',
      padding: '1.25rem .75rem',
    },
  },
  headerContainer: {
    display: 'flex',
    flexDirection: 'column',
    [theme.breakpoints.down('md')]: {
      alignItems: 'center',
    },
  },
  header1: {
    display: 'flex',
    alignItems: 'center',
    marginBottom: '.5rem',
  },
  header2: {
    textAlign: 'left',
    maxWidth: '75%',
    [theme.breakpoints.down('sm')]: {
      textAlign: 'center',
      marginBottom: '.5rem',
      maxWidth: '100%',
    },
  },
  subTitle: {
    textAlign: 'left',
    fontSize: '1rem',
    color: theme.palette.grey.A300,
    '& span': {
      color: theme.palette.global.magenta,
    },
    [theme.breakpoints.down('md')]: {
      margin: '.5rem 0',
    },
    [theme.breakpoints.down('sm')]: {
      textAlign: 'center',
    },
  },
  title: {
    color: theme.palette.grey.A300,
    fontSize: '1.5rem',
    padding: 0,
    [theme.breakpoints.down('md')]: {
      fontSize: '1.25rem',
    },
  },
  toolTip: {
    display: 'inline-block',
  },
  infoIcon: {
    color: theme.palette.primary.main,
    verticalAlign: 'top',
    marginLeft: '.5rem',
    [theme.breakpoints.down('md')]: {
      verticalAlign: 'bottom',
    },
  },
  bannerBar: {
    position: 'absolute',
    width: '100%',
    height: '0.25rem',
    bottom: 0,
    left: 0,
    backgroundColor: theme.palette.global.magenta,
  },
  bannerImage: {
    marginRight: 14,
    width: 29,
    height: 29,
    filter: `invert(0%) sepia(86%) saturate(7491%) hue-rotate(177deg) brightness(0) contrast(99%)`,
  },
  bannerBtn: {
    whiteSpace: 'nowrap',
    borderColor: theme.palette.global.magenta,
    color: theme.palette.common.white,
    backgroundColor: theme.palette.global.magenta,
    [theme.breakpoints.down('md')]: {
      fontSize: '1rem',
    },
    minWidth: 'min-content',
    '&:hover': {
      color: theme.palette.common.white,
      borderColor: theme.palette.global.magenta,
      backgroundColor: theme.palette.global.magenta,
    },
  },
  dealOptionContainer: {
    display: 'flex',
    justifyContent: 'flex-end',
    flexDirection: 'row',
    flexWrap: 'wrap',
    paddingTop: '.5rem',
    [theme.breakpoints.down('md')]: {
      justifyContent: 'center',
    },
  },
  dealOption: {
    justifyContent: 'space-between',
    alignItems: 'center',
    display: 'block',
    textAlign: 'left',
    margin: '0 0.5rem 0 1rem',
    [theme.breakpoints.down('sm')]: {
      margin: '.5rem .5rem 0 .5rem',
    },
  },
  dealTitleText: {
    fontSize: '0.75rem',
    fontWeight: 500,
    margin: '0 0 .2rem .2rem',
  },
  dropDownOptions: {
    '& .MuiSelect-select:focus': {
      backgroundColor: theme.palette.common.white,
    },
  },
  tradeInContainer: {
    textAlign: 'left',
    marginTop: '.2rem!important',
    [theme.breakpoints.down('md')]: {
      margin: '.4rem 1rem!important',
    },
    [theme.breakpoints.down('sm')]: {
      margin: '1rem .5rem 0 .5rem!important',
    },
  },
  tradeInText: {
    fontSize: '0.875rem',
    fontWeight: 600,
  },
  tradeInAmount: {
    fontSize: '0.875rem',
    fontWeight: 600,
    display: 'inline-block',
    alignItems: 'center',
    whiteSpace: 'nowrap',
    paddingTop: '.1rem',
  },
  tradeInIconContainer: {
    paddingTop: 5,
  },
  tradeInDeleteIcon: {
    fontSize: 25,
    marginRight: -theme.spacing(1.5),
    marginLeft: -theme.spacing(1),
  },
  legalText: {
    fontSize: '0.625rem',
    fontWeight: 500,
    margin: '0 0 0 8px',
    textAlign: 'right',
    [theme.breakpoints.down('md')]: {
      textAlign: 'center',
    },
    [theme.breakpoints.down('sm')]: {
      marginLeft: '1.5rem',
      marginRight: '1.5rem',
    },
  },
  legalContainer: {
    flexBasis: '100%',
    marginTop: '0.25rem',
    [theme.breakpoints.down('sm')]: {
      marginTop: '0.5rem',
    },
  },
}));

export default useStyles;
