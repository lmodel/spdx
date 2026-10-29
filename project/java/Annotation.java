package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An assertion made in relation to one or more elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Annotation extends Element {

  private String contentType;
  private String annotationType;
  private String statement;
  private Element subject;


}