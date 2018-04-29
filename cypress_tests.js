//cypress tests for viewport, email test, retirement test, and split the tip test

 context('Viewport', function () {
    beforeEach(function () {
      cy.visit('http://35.196.89.171/menu.html')
    })

    it('Alter the viewport size and dimension', function () {

      //cy.get('#navbar').should('be.visible')

      // https://on.cypress.io/viewport
      cy.viewport(320, 480)

      // lets see what our app looks like on a super large screen
      cy.viewport(2999, 2999)

      // cy.viewport() accepts a set of preset sizes
      // to easily set the screen to a device's width and height

      // We added a cy.wait() between each viewport change so you can see
      // the change otherwise it's a little too fast to see :)

      cy.viewport('macbook-15')
      cy.wait(200)
      cy.viewport('macbook-13')
      cy.wait(200)
      cy.viewport('macbook-11')
      cy.wait(200)
      cy.viewport('ipad-2')
      cy.wait(200)
      cy.viewport('ipad-mini')
      cy.wait(200)
      cy.viewport('iphone-6+')
      cy.wait(200)
      cy.viewport('iphone-6')
      cy.wait(200)
      cy.viewport('iphone-5')
      cy.wait(200)
      cy.viewport('iphone-4')
      cy.wait(200)
      cy.viewport('iphone-3')
      cy.wait(200)

      // cy.viewport() accepts an orientation for all presets
      // the default orientation is 'portrait'
      cy.viewport('ipad-2', 'portrait')
      cy.wait(200)
      cy.viewport('iphone-4', 'landscape')
      cy.wait(200)
      cy.viewport('macbook-15')
      // The viewport will be reset back to the default dimensions
      // in between tests (the  default is set in cypress.json)
    })
  })

describe('Menu test', function(){
  it('Visits the BMI site', function(){
    cy.contains('Body Mass Index').click()
    cy.url().should('include', '/bmi.html')})

  it('Go back to the menu', function (){
    cy.contains('Go Back').click()
    cy.url().should('include', '/menu.html')})

  it('Visits the retirement site', function(){
    cy.contains('Retirement').click()
    cy.url().should('include', '/retire.html')})

  it('Go back to the menu', function (){
    cy.contains('Go Back').click()
    cy.url().should('include', '/menu.html')})

  it('Visits the shortest distance site', function(){
    cy.contains('Shortest Distance').click()
    cy.url().should('include', '/short.html')})

  it('Go back to the menu', function (){
    cy.contains('Go Back').click()
    cy.url().should('include', '/menu.html')})

  it('Visits the email verifier site', function(){
    cy.contains('Email Verifier').click()
    cy.url().should('include', '/email.html')})

  it('Go back to the menu', function (){
    cy.contains('Go Back').click()
    cy.url().should('include', '/menu.html')})

  it('Visits the split the tip site', function(){
    cy.contains('Split the Tip').click()
    cy.url().should('include', '/split.html')})

  it('Go back to the menu', function (){
    cy.contains('Go back').click()
    cy.url().should('include', '/menu.html')})


  })

describe('BMI test', function(){
  it('Visits the BMI site', function(){
    cy.contains('Body Mass Index').click()
    cy.url().should('include', '/bmi.html')})

  it('Type in feet', function (){
    cy.get('#feet')
      .type('5').should('have.value', '5')})

  it('Type in inches', function (){
    cy.get('#inch')
      .type('6').should('have.value', '6')})

  it('Type in weight', function (){
    cy.get('#weight')
      .type('150').should('have.value', '150')})

  it('Compute BMI', function (){
    cy.contains('Compute BMI').click()
    cy.url().should('include', '/cgi-bin/function1.py')})

  it('Go back to the menu', function (){
    cy.visit('35.196.89.171/email.html')
    cy.contains('Go Back').click()
    cy.url().should('include', '/menu.html')})

  })


describe('Retirement test', function(){
  it('Visits the retirement site', function(){
    cy.visit('35.196.89.171/retire.html')})

  it('Type in an age', function (){
    cy.get('#age')
      .type('30').should('have.value', '30')})

  it('Type in salary', function (){
    cy.get('#sal')
      .type('100000').should('have.value', '100000')})

  it('Type in saved percentage', function (){
    cy.get('#save')
      .type('10').should('have.value', '10')})

  it('Type in goal amount', function (){
    cy.get('#goal')
      .type('500000').should('have.value', '500000')})

  it('Caluculate Goal', function (){
    cy.contains('Calculate').click()
    cy.url().should('include', '/cgi-bin/function2.py')})

  it('Go back to the menu', function (){
    cy.visit('35.196.89.171/retire.html')
    cy.contains('Go Back').click()
    cy.url().should('include', 'menu.html')})

  })

describe('Shortest Distance test', function(){
  it('Visits the SD site', function(){
    cy.contains('Shortest').click()
    cy.url().should('include', '/short.html')})

  it('Enter x1:', function (){
    cy.get('#x1')
      .type('30').should('have.value', '30')})

  it('Enter y1', function (){
    cy.get('#y1')
      .type('100000').should('have.value', '100000')})

  it('Enter x2', function (){
    cy.get('#x2')
      .type('10').should('have.value', '10')})

  it('Enter y2', function (){
    cy.get('#y2')
      .type('500000').should('have.value', '500000')})

  it('Caluculate SD', function (){
    cy.contains('Calculate').click()
    cy.url().should('include', '/cgi-bin/function3.py')})

  it('Go back to the menu', function (){
    cy.visit('35.196.89.171/short.html')
    cy.contains('Go Back').click()
    cy.url().should('include', 'menu.html')})

  })

describe('Email test', function(){
  it('Visits the email site', function(){
    cy.visit('35.196.89.171/email.html')})

  it('Type in an address', function (){
    cy.get('#address')
      .type('fake@email.com').should('have.value', 'fake@email.com')})

  it('Verify email address', function (){
    cy.contains('Verify').click()
    cy.url().should('include', '/cgi-bin/function4.py')})

  it('Go back to the menu', function (){
    cy.visit('35.196.89.171/email.html')
    cy.contains('Go Back').click()
    cy.url().should('be', 'http://35.196.89.171/menu.html')})

  })

describe('Split the Tip test', function(){
  it('Visits the split site', function(){
    cy.visit('35.196.89.171/split.html')})

  it('Enter total amount', function (){
    cy.get('#num1')
      .type('50').should('have.value', '50')})

  it('Enter total guests', function (){
    cy.get('#num2')
      .type('3').should('have.value', '3')})

  it('Split tip', function (){
    cy.contains('Split the').click()
    cy.url().should('include', '/cgi-bin/function5.py')})

  it('Go back to the menu', function (){
    cy.visit('35.196.89.171/email.html')
    cy.contains('Go Back').click()
    cy.url().should('be', 'http://35.196.89.171/menu.html')})

  })

